class BaseModel:
    def __init__(self, id: int = None):
        self.id = id

    def get_id(self):
        return self.id