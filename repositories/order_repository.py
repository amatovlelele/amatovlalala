from db.database import get_connection
from models.order import Order

class OrderRepository:
    def create(self, order: Order):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO orders (user_id, total) VALUES (?, ?)", 
                           (order.user_id, order.total))
            order.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

    def update(self, order_id: int, total: float):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE orders SET total = ? WHERE id = ?", (total, order_id))
            conn.commit()
        finally:
            conn.close()

    def delete(self, order_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
            conn.commit()
        finally:
            conn.close()

    def get_orders_with_users(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM user_orders") # Используем VIEW
            return cursor.fetchall()
        finally:
            conn.close()

    def get_total_by_user(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT user_id, SUM(total) FROM orders GROUP BY user_id
            """)
            return cursor.fetchall()
        finally:
            conn.close()