import mysql.connector
from mysql.connector import Error
from create_db import DB_CONFIG, DB_NAME

def insert_10_users(db_name=DB_NAME):
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG, database=db_name)
        
        if connection.is_connected():
            with connection.cursor() as cursor:
                
                insert_query = """
                INSERT INTO users (username, last_name, first_name, middle_name, email, phone)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
                users_data = [
                    ("ivan_90", "Иванов", "Иван", "Иванович", "ivan@example.com", "+79991112233"),
                    ("alex_smith", "Петров", "Алексей", None, "alex@example.com", "+79992223344"),
                    ("anna_key", "Сидорова", "Анна", "Сергеевна", "anna@example.com", "+79993334455"),
                    ("dmitry_v", "Васильев", "Дмитрий", "Николаевич", "dmitry@example.com", "+79994445566"),
                    ("elena_p", "Павлова", "Елена", None, "elena@example.com", "+79995556677"),
                    ("serg_k", "Кузнецов", "Сергей", "Петрович", "sergey@example.com", "+79996667788"),
                    ("olga_m", "Морозова", "Ольга", "Александровна", "olga@example.com", "+79997778899"),
                    ("artem_f", "Федоров", "Артем", None, "artem@example.com", "+79998889900"),
                    ("nataly_s", "Соколова", "Наталья", "Дмитриевна", "nataly@example.com", "+79999990011"),
                    ("max_code", "Попов", "Максим", "Игоревич", "max@example.com", "+79990001122")
                ]
                
                print("Выполняю массовую вставку пользователей...")
                cursor.executemany(insert_query, users_data)
                
                connection.commit()
                
                print(f"Успешно добавлено пользователей: {cursor.rowcount}")

    except Error as err:
        print(f"Ошибка при вставке данных: {err}")
        if connection and connection.is_connected():
            connection.rollback()
            print("Транзакция отменена из-за ошибки.")
            
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Соединение с базой данных закрыто.")

if __name__ == "__main__":
    insert_10_users()
