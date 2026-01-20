from models.base import BaseModel


class Order(BaseModel):
    def __init__(self, user_id: int, total: float, id: int = None):
        super().__init__(id)
        self.user_id = user_id
        self.total = total