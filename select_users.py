import mysql.connector
from mysql.connector import Error
from create_db import DB_CONFIG, DB_NAME

def get_users(db_name=DB_NAME):
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG, database=db_name)
        
        if connection.is_connected():
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, first_name, last_name, email FROM users;")
                users = cursor.fetchall()
                
                if not users:
                    print("Таблица пуста.")
                    return
                
                print("\nСписок пользователей в базе данных:")
                print("=" * 60)
                for user in users:
                    print(f"ID: {user[0]} | Логин: {user[1]} | Имя: {user[2]} {user[3]} | Email: {user[4]}")
                print("=" * 60)

    except Error as err:
        print(f"Ошибка чтения данных: {err}")
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    get_users()