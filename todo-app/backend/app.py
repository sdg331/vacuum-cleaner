"""
Flask Todo API - Production Ready Single File Version

개선 사항:
✅ Pagination (페이지네이션) 추가
✅ 다중 필터링 & 정렬 기능
✅ 입력 검증 강화
✅ 전역 에러 핸들링
✅ 트랜잭션 롤백 처리
✅ API 문서화 주석 (Docstring)
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

# =========================================
# Flask 앱 및 기본 설정
# =========================================
app = Flask(__name__)

from config import get_config

# config.py의 설정을 로드합니다.
app.config.from_object(get_config())

# CORS 설정 (개발용: 전체 허용)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# SQLAlchemy 초기화
db = SQLAlchemy(app)


# =========================================
# 데이터베이스 모델
# =========================================
class Todo(db.Model):
    """할 일 모델 (todos 테이블)"""
    
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow, 
        nullable=False
    )

    def to_dict(self):
        """JSON 직렬화용 딕셔너리 변환"""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


# 앱 시작 시 테이블 자동 생성 (개발용)
with app.app_context():
    db.create_all()


# =========================================
# 헬퍼 함수 (Helper Functions)
# =========================================

def validate_title(title):
    """
    제목 유효성 검사 헬퍼
    
    Args:
        title (str): 검사할 제목
        
    Returns:
        tuple: (성공 여부, 에러 메시지)
    """
    if not title or not title.strip():
        return False, "title is required"
    
    if len(title) > 255:
        return False, "title is too long (max 255 characters)"
    
    return True, None


def parse_pagination():
    """
    페이지네이션 파라미터 파싱
    
    Query Parameters:
        page (int): 페이지 번호 (기본값: 1)
        per_page (int): 페이지당 항목 수 (기본값: 10, 최대: 100)
        
    Returns:
        tuple: (page, per_page)
    """
    try:
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))
        
        # 범위 제한 (보안)
        page = max(1, page)
        per_page = max(1, min(per_page, 100))  # 최대 100개 제한
        
        return page, per_page
    except ValueError:
        return 1, 10  # 잘못된 값이면 기본값 반환


def build_todo_query():
    """
    [✨ 신규] Todo 쿼리 빌더 (필터링 + 정렬)
    
    Query Parameters:
        completed (str): "true" / "false" - 완료 상태 필터링
        search (str): 제목 검색어 (부분 일치)
        sort (str): 정렬 필드 (created_at/updated_at/title)
        order (str): 정렬 순서 (asc/desc)
        
    Returns:
        Query: 빌드된 SQLAlchemy 쿼리 객체
    """
    query = Todo.query
    
    # [필터 1] 완료 상태 필터링
    completed_param = request.args.get("completed")
    if completed_param:
        if completed_param.lower() == "true":
            query = query.filter_by(completed=True)
        elif completed_param.lower() == "false":
            query = query.filter_by(completed=False)
    
    # [필터 2] 제목 검색 (LIKE 검색)
    search_term = request.args.get("search", "").strip()
    if search_term:
        query = query.filter(Todo.title.ilike(f"%{search_term}%"))
    
    # [정렬] 다중 필드 정렬 지원
    sort_field = request.args.get("sort", "created_at")
    sort_order = request.args.get("order", "desc")
    
    # 허용된 필드만 정렬 (SQL Injection 방지)
    allowed_fields = ["created_at", "updated_at", "title", "completed"]
    if sort_field in allowed_fields:
        column = getattr(Todo, sort_field)
        if sort_order == "asc":
            query = query.order_by(column.asc())
        else:
            query = query.order_by(column.desc())
    else:
        # 기본값: 최신순
        query = query.order_by(Todo.created_at.desc())
    
    return query


# =========================================
# 전역 에러 핸들러
# =========================================

@app.errorhandler(404)
def not_found_error(error):
    """404 Not Found 처리"""
    return jsonify({
        "error": "Resource not found",
        "status_code": 404
    }), 404


@app.errorhandler(400)
def bad_request_error(error):
    """400 Bad Request 처리"""
    return jsonify({
        "error": "Bad request",
        "message": str(error),
        "status_code": 400
    }), 400


@app.errorhandler(500)
def internal_error(error):
    """500 Internal Server Error 처리"""
    db.session.rollback()  # 에러 발생 시 롤백
    return jsonify({
        "error": "Internal server error",
        "status_code": 500
    }), 500


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    """모든 HTTP 예외 통합 처리"""
    return jsonify({
        "error": error.description,
        "status_code": error.code
    }), error.code


# app.py: @app.errorhandler(Exception) 내부 수정

@app.errorhandler(Exception)
def handle_unexpected_error(error):
    """예상치 못한 에러 처리"""
    db.session.rollback()
    
    # --- [변경 시작: 로거 활성화] ---
    # 🚨 변경: 주석을 제거하여 Flask Logger를 통해 에러를 기록합니다.
    app.logger.error(f"Unexpected error: {error}")
    # --- [변경 끝] ---
    
    return jsonify({
        "error": "An unexpected error occurred",
        "status_code": 500
    }), 500


# =========================================
# API 엔드포인트
# =========================================

@app.route("/api/health", methods=["GET"])
def health_check():
    """서버 상태 확인용 헬스 체크"""
    return jsonify({
        "status": "ok",
        "message": "Todo API is running"
    }), 200


@app.route("/api/todos", methods=["GET"])
def get_todos():
    """
    [✨ 개선] 모든 할 일 조회 (페이지네이션 + 필터링 + 정렬)
    
    Query Parameters:
        - page (int): 페이지 번호 (기본값: 1)
        - per_page (int): 페이지당 항목 수 (기본값: 10, 최대: 100)
        - completed (str): "true" / "false" - 완료 상태 필터링
        - search (str): 제목 검색어 (부분 일치, 대소문자 무시)
        - sort (str): 정렬 필드 (created_at/updated_at/title/completed)
        - order (str): 정렬 순서 (asc/desc, 기본값: desc)
    
    Examples:
        GET /api/todos
        GET /api/todos?page=2&per_page=20
        GET /api/todos?completed=false&search=공부&sort=title&order=asc
    
    Response:
        {
            "data": [
                {
                    "id": 1,
                    "title": "Flask 공부하기",
                    "completed": false,
                    "created_at": "2025-12-07T12:00:00",
                    "updated_at": "2025-12-07T12:00:00"
                }
            ],
            "pagination": {
                "page": 1,
                "per_page": 10,
                "total": 50,
                "total_pages": 5
            }
        }
    """
    try:
        # 쿼리 빌드 (필터링 + 정렬)
        query = build_todo_query()
        
        # 페이지네이션 파라미터 파싱
        page, per_page = parse_pagination()
        
        # 페이지네이션 실행
        pagination = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False  # 페이지 초과 시 빈 리스트 반환
        )
        
        return jsonify({
            "data": [todo.to_dict() for todo in pagination.items],
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total": pagination.total,
                "total_pages": pagination.pages
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": "Failed to fetch todos",
            "detail": str(e)
        }), 500


@app.route("/api/todos", methods=["POST"])
def create_todo():
    """
    [✨ 개선] 할 일 추가 (입력 검증 강화)
    
    Request Body:
        {
            "title": "새로운 할 일"
        }
    
    Response:
        - 201: 생성 성공 + 생성된 객체 반환
        - 400: 잘못된 요청 (title 누락, 길이 초과 등)
        - 500: 서버 에러
    """
    data = request.get_json(silent=True) or {}
    
    title = data.get("title", "").strip()
    
    # 입력 검증
    is_valid, error_msg = validate_title(title)
    if not is_valid:
        return jsonify({"error": error_msg}), 400
    
    try:
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
        
        return jsonify(todo.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to create todo",
            "detail": str(e)
        }), 500


@app.route("/api/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    """
    [✨ 신규] 특정 할 일 조회
    
    Path Parameter:
        todo_id (int): Todo ID
    
    Response:
        - 200: 조회 성공
        - 404: Todo 없음
    """
    todo = Todo.query.get(todo_id)
    
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    return jsonify(todo.to_dict()), 200


# app.py: def update_todo(todo_id) 내부 수정

@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    """특정 할 일 수정 (트랜잭션 안전성 강화)"""
    todo = Todo.query.get(todo_id)
    
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    data = request.get_json(silent=True) or {}
    
    # title 수정 (선택 사항)
    if "title" in data:
        new_title = str(data["title"]).strip()
        
        is_valid, error_msg = validate_title(new_title)
        if not is_valid:
            # --- [변경 시작: 400 상태 코드를 명시적으로 반환] ---
            # 🚨 변경: 제목 검증 실패 시 400 Bad Request 명시적 반환
            return jsonify({"error": error_msg}), 400 
            # --- [변경 끝] ---
            
        todo.title = new_title
        
    # completed 수정 (선택 사항)
    if "completed" in data:
        todo.completed = bool(data["completed"])
        
    try:
        db.session.commit()
        return jsonify(todo.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to update todo",
            "detail": str(e)
        }), 500


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    """
    특정 할 일 삭제
    
    Response:
        - 204: 삭제 성공 (응답 본문 없음)
        - 404: Todo 없음
        - 500: 서버 에러
    """
    todo = Todo.query.get(todo_id)
    
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    try:
        db.session.delete(todo)
        db.session.commit()
        return "", 204
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to delete todo",
            "detail": str(e)
        }), 500


# app.py: @app.route("/api/todos", methods=["DELETE"]) 내부 수정

@app.route("/api/todos", methods=["DELETE"])
def delete_all_todos():
    """
    [⚠️ 주의] 모든 할 일 삭제 (개발/디버그용)
    프로덕션 환경에서는 비활성화 권장
    """
    try:
        deleted_count = Todo.query.delete()
        db.session.commit()
        
        # --- [변경 시작: 204 응답으로 변경] ---
        # 🚨 변경: 삭제 성공 시 응답 본문 없이 204 No Content를 반환합니다.
        return "", 204 
        # --- [변경 끝] ---
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to delete todos",
            "detail": str(e)
        }), 500
# app.py (새로운 헬퍼 함수 추가)

def create_initial_tables(app):
    """
    애플리케이션 컨텍스트 내에서 데이터베이스 테이블을 생성합니다.
    (개발 환경 초기화용)
    """
    with app.app_context():
        db.create_all()

# =========================================
# 메인 실행
# =========================================
# app.py: if __name__ == "__main__": 블록 수정

if __name__ == "__main__":
    app = create_app() # (1단계 커밋에서 변경된 내용)
    
    # with app.app_context(): db.create_all() <--- 이 부분을 제거하고 다음 코드로 대체
    # --- [변경 시작] ---
    # 🚨 변경: 헬퍼 함수 호출로 대체
    create_initial_tables(app)
    # --- [변경 끝] ---
    
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=app.config['DEBUG']
    )
