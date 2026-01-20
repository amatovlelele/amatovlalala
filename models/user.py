from models.base import BaseModel

class User(BaseModel):
    def __init__(self, name: str, id: int = None):
        super().__init__(id)
        self.name = name

    def __str__(self):
        return f"User (id={self.id}, name={self.name})"