from pydantic import BaseModel


class UserMatrixOutSchema(BaseModel):
    name: str
    height: int
    width: int

    class Config:
        json_schema_extra = {
            'example': {
                'name': 'awrura',
                'height': 16,
                'width': 16,
            }
        }
