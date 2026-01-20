from db.database import get_connection
from models.user import User

class UserRepository:
    def create(self, user: User):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name) VALUES (?)", (user.name,))
            user.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, name FROM users")
            rows = cursor.fetchall()
            return [User(id=row[0], name=row[1]) for row in rows]
        finally:
            conn.close()