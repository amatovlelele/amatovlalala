from db.database import init_db
from models.user import User
from models.product import Product
from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.order_repository import OrderRepository
from services.order_service import OrderService

def main():
    init_db()

   
    user_repo = UserRepository()
    product_repo = ProductRepository()
    order_repo = OrderRepository()
    order_service = OrderService()

    
    user = User(name="Bob")
    user_repo.create(user)
    print(f"Создан пользователь: {user}")

    
    product = Product(name="Burger", price=250)
    product_repo.create(product)
    print(f"Создан товар: {product.name}, Цена: {product.get_price()}")

    
    order_service.create_order(user_id=user.id, total=250)
    order_service.create_order(user_id=user.id, total=-100) 

   
    print("\n--- Список заказов (User + Total) ---")
    orders_data = order_repo.get_orders_with_users()
    for row in orders_data:
        print(f"Пользователь: {row[0]}, Сумма: {row[1]}")

    
    print("\n--- Статистика по пользователям ---")
    stats = order_repo.get_total_by_user()
    for row in stats:
        print(f"User ID: {row[0]}, Общая сумма: {row[1]}")

if __name__ == "__main__":
    main()
