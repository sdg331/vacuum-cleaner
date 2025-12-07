# schemas.py (신규 생성 파일 - 전체 복사/붙여넣기)

from marshmallow import Schema, fields, validate
# datetime은 Marshmallow fields.DateTime 때문에 필요합니다.
# from datetime import datetime 

class TodoSchema(Schema):
    """
    Todo 객체의 직렬화/역직렬화 및 유효성 검증 스키마
    """
    # dump_only=True: 출력을 위해서만 사용 (DB에서 생성)
    id = fields.Int(dump_only=True)
    
    # required=True: 입력 필수, validate: 입력 길이 제한
    title = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, max=255, error="Title must be between 1 and 255 characters."),
        ]
    )
    # load_default=False: 입력 없으면 False로 간주
    completed = fields.Bool(load_default=False)
    
    # dump_only=True: 출력 전용 필드
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# API 응답에서 단일 Todo 객체를 직렬화할 때 사용
todo_schema = TodoSchema()
# API 응답에서 Todo 객체 리스트를 직렬화할 때 사용
todos_schema = TodoSchema(many=True)
