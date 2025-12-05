from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

from config import get_database_uri
from dotenv import load_dotenv
load_dotenv()

# -------------------------------------------------
# Flask 앱 및 기본 설정
# -------------------------------------------------
app = Flask(__name__)

# 환경변수에서 DB URL 읽기 (없으면 기본값 사용)
# 형식: mysql+pymysql://user:password@host:port/database
DB_USER = os.getenv("DB_USER", "todo_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "todo_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "todo_db")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# CORS 허용 (개발용: 전체 허용)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# SQLAlchemy 초기화
db = SQLAlchemy(app)


# -------------------------------------------------
# 데이터베이스 모델
# -------------------------------------------------
class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def to_dict(self):
        """객체를 JSON 직렬화 가능한 dict로 변환."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


# 앱 시작 시 테이블 생성 (마이그레이션 없이 간단 버전)
with app.app_context():
    db.create_all()


# -------------------------------------------------
# 헬스 체크용 엔드포인트
# -------------------------------------------------
@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


# -------------------------------------------------
# Todo CRUD API
# 베이스 URL: /api/todos
# -------------------------------------------------

# 1) 모든 할 일 조회 (Read)
@app.route("/api/todos", methods=["GET"])
def get_todos():
    """
    쿼리 파라미터:
      - completed: "true" / "false" (선택)
    예:
      /api/todos
      /api/todos?completed=true
    """
    completed_param = request.args.get("completed")

    query = Todo.query

    if completed_param is not None:
        if completed_param.lower() == "true":
            query = query.filter_by(completed=True)
        elif completed_param.lower() == "false":
            query = query.filter_by(completed=False)

    todos = query.order_by(Todo.created_at.desc()).all()
    return jsonify([todo.to_dict() for todo in todos]), 200


# 2) 할 일 추가 (Create)
@app.route("/api/todos", methods=["POST"])
def create_todo():
    """
    요청 JSON 예:
    {
      "title": "새로운 할 일"
    }
    """
    data = request.get_json(silent=True) or {}

    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "title is required"}), 400

    if len(title) > 255:
        return jsonify({"error": "title is too long (max 255)"}), 400

    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.to_dict()), 201


# 3) 특정 할 일 수정 (Update)
@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id: int):
    """
    요청 JSON 예:
    {
      "title": "제목 수정",
      "completed": true
    }
    """
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json(silent=True) or {}

    # title 수정 (옵션)
    if "title" in data:
        new_title = str(data["title"]).strip()
        if not new_title:
            return jsonify({"error": "title cannot be empty"}), 400
        if len(new_title) > 255:
            return jsonify({"error": "title is too long (max 255)"}), 400
        todo.title = new_title

    # completed 수정 (옵션)
    if "completed" in data:
        # 강제로 bool 변환
        todo.completed = bool(data["completed"])

    db.session.commit()
    return jsonify(todo.to_dict()), 200


# 4) 특정 할 일 삭제 (Delete)
@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()
    return "", 204


# 5) 모든 할 일 삭제 (선택 기능, 개발/디버그용)
@app.route("/api/todos", methods=["DELETE"])
def delete_all_todos():
    deleted_count = Todo.query.delete()
    db.session.commit()
    return jsonify({"deleted": deleted_count}), 200


# -------------------------------------------------
# 메인 실행
# -------------------------------------------------
if __name__ == "__main__":
    # 개발용 설정: 자동 리로드 + 디버그
    app.run(host="0.0.0.0", port=5000, debug=True)

# -------------------------------------------------

''' 
필요한 파이썬 패키지 
Flask==3.0.0
Flask-CORS==4.0.0
Flask-SQLAlchemy==3.1.1
PyMySQL==1.1.0
python-dotenv==1.0.1
'''

'''
MySQL 쪽 최소 준비 사항
-- MySQL 접속 후 (root 등으로)
CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'todo_user'@'localhost' IDENTIFIED BY 'todo_password';

GRANT ALL PRIVILEGES ON todo_db.* TO 'todo_user'@'localhost';

FLUSH PRIVILEGES;

app.py에서 쓴 설정과 맞아야 함
DB_USER = "todo_user"
DB_PASSWORD = "todo_password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "todo_db"

'''

'''
빠른 체크리스트 (실행 테스트)
가상환경 생성 + 패키지 설치

bash
cd backend
pip install -r requirements.txt
MySQL에서 DB/USER 생성 (위 SQL 실행)

서버 실행

bash
python app.py
브라우저에서 확인

http://localhost:5000/api/health → {"status": "ok"} 나오면 성공

Postman / VSCode REST Client / curl로 테스트

GET http://localhost:5000/api/todos

POST http://localhost:5000/api/todos with JSON {"title": "테스트"}
'''
