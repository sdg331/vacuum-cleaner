-- DB와 사용자, 테이블을 한 번에 만드는 초기화 스크립트

-- 1) 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS todo_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2) 사용자 생성 (이미 있으면 에러 날 수 있으니 상황에 따라 생략 가능)
CREATE USER IF NOT EXISTS 'todo_user'@'localhost'
  IDENTIFIED BY 'todo_password';

GRANT ALL PRIVILEGES ON todo_db.* TO 'todo_user'@'localhost';
FLUSH PRIVILEGES;

-- 3) 사용할 DB 선택
USE todo_db;

-- 4) todos 테이블 생성
CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed TINYINT(1) NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
