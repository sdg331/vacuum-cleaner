## 요약
GitHub README.md에 적합하게 실행 방법을 한국어로 깔끔하게 정리했다. 이모티콘 없이 전문적인 형식으로 구성했으며, 코드 블록과 표를 활용하여 가독성을 높였다.

***

아래 내용을 그대로 README.md에 복사하여 사용하면 된다.

```markdown
# 실행 방법

## 사전 요구 사항
- MySQL 8.0 이상
- Python 3.10 이상
- Node.js 18 이상

---

## 1. 데이터베이스 설정 (MySQL)

### 1-1. MySQL 서버 실행
로컬에 MySQL이 설치되어 있어야 한다.

**MySQL 실행 여부 확인:**
```
mysql -u root -p
```
비밀번호 입력 후 접속되면 정상이다.

### 1-2. 데이터베이스, 사용자, 테이블 생성
프로젝트 루트에서 초기화 스크립트를 실행한다:

```
SOURCE /절대/경로/todo-app/db/init.sql;
```

**또는 직접 실행:**
```
CREATE DATABASE IF NOT EXISTS todo_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'todo_user'@'localhost'
  IDENTIFIED BY 'todo_password';

GRANT ALL PRIVILEGES ON todo_db.* TO 'todo_user'@'localhost';
FLUSH PRIVILEGES;

USE todo_db;

CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed TINYINT(1) NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 2. 백엔드 설정 (Flask)

### 2-1. 가상환경 생성 (권장)
```
cd todo-app/backend

# venv 생성 (최초 1회)
python -m venv venv

# 활성화 (Windows)
venv\Scripts\activate

# 활성화 (macOS/Linux)
source venv/bin/activate
```

### 2-2. 패키지 설치
```
pip install -r requirements.txt
```

### 2-3. 환경 변수 설정
`todo-app/backend/.env` 파일 생성:

```
DB_USER=todo_user
DB_PASSWORD=todo_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=todo_db
```

> `app.py` 상단에 다음 코드가 포함되어 있는지 확인:
> ```
> from dotenv import load_dotenv
> load_dotenv()
> ```

### 2-4. Flask 서버 실행
```
python app.py
```

**정상 출력 예시:**
```
Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

### 2-5. 백엔드 동작 확인
브라우저에서 접속:
```
http://localhost:5000/api/health
```

**정상 응답:**
```
{"status": "ok"}
```

---

## 3. 프론트엔드 설정 (Vite + React)

### 3-1. 의존성 설치
```
cd todo-app/frontend
npm install
```

### 3-2. 개발 서버 실행
```
npm run dev
```

**정상 출력 예시:**
```
Local: http://localhost:5173/
```

### 3-3. 애플리케이션 테스트
브라우저에서 `http://localhost:5173` 접속

| 동작 | 예상 결과 |
|------|-----------|
| 할 일 추가 | 목록에 항목 표시 (`POST /api/todos`) |
| 체크박스 클릭 | 텍스트 취소선 표시 (`PUT /api/todos/{id}`) |
| 삭제 버튼 클릭 | 항목 제거 (`DELETE /api/todos/{id}`) |

---

## 실행 순서 요약

| 단계 | 명령어 |
|------|--------|
| 1. DB 설정 | MySQL에서 `db/init.sql` 실행 |
| 2. 백엔드 | `cd backend` → `pip install -r requirements.txt` → `python app.py` |
| 3. 프론트엔드 | `cd frontend` → `npm install` → `npm run dev` |
| 4. 접속 | http://localhost:5173 |

---

## 문제 해결

| 오류 | 해결 방법 |
|------|-----------|
| `ModuleNotFoundError: No module named 'flask'` | `pip install -r requirements.txt` 실행 또는 venv 활성화 |
| `Access denied for user` | `.env` 파일의 DB 계정 정보 확인 |
| 브라우저 콘솔에 `CORS error` | 백엔드에서 `CORS(app, resources={r"/api/*": {"origins": "*"}})` 설정 확인 |
| 프론트엔드에서 `Failed to fetch` | 백엔드 서버가 5000 포트에서 실행 중인지 확인 |
```
