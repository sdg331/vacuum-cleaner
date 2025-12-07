[models.py내용 업데이트함]
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# db 객체를 여기서 생성 (순환 참조 방지)
db = SQLAlchemy()

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
