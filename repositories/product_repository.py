from db.database import get_connection
from models.product import Product

class ProductRepository:
    def create(self, product: Product):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", 
                           (product.name, product.get_price()))
            product.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()