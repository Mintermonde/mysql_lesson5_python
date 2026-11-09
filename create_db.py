import os
import mysql.connector
import time
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="secret",
        database="demo_lesson5_db",
        charset="utf8mb4",
        autocommit=False
    )

    if connection.is_connected():
        print("Успешное подключение к серверу MySQL!")
        print(f"Версия сервера: {connection.get_server_info()}")

except Error as err:
    print(f"Ошибка подключения: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Соединение с базой данных закрыто.")


DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", 3306)),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "secret"),
    "charset": "utf8mb4"
}

DB_NAME = "demo_lesson5_db"

def create_database(db_name=DB_NAME, retries=10, delay=3):
    connection = None
    for attempt in range(1, retries + 1):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            break
        except Error as err:
            if attempt == retries:
                raise
            print(f"Сервер MYSQL недоступен ({err}), попытка {attempt}/{retries}...")
            time.sleep(delay)

    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{db_name}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
        )
        cursor.execute("SHOW DATABASES LIKE %s;", (db_name,))
        if cursor.fetchone():
            print(f"База данных `{db_name}` готова к работе")
        cursor.close()
    finally:
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()