from repositories.order_repository import OrderRepository
from models.order import Order

class OrderService:
    def __init__(self):
        self.repo = OrderRepository()

    def create_order(self, user_id: int, total: float):
        
        if total <= 0:
            print("Ошибка: Сумма заказа должна быть положительной!")
            return None
        
        try:
            order = Order(user_id=user_id, total=total)
            self.repo.create(order)
            print(f"Заказ успешно создан: ID {order.id}, Сумма {order.total}")
            return order
        except Exception as e:
            print(f"Ошибка при создании заказа: {e}")