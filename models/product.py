from models.base import BaseModel


class Product(BaseModel):
    def __init__(self, name: str, price: float, id: int = None):
        super().__init__(id)
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должно быть меньше 0!")
        self.__price = new_price