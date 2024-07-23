import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dogtorken"
        )

        if db.is_connected():
            mycursor = db.cursor()
            
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            mycursor.close()
            db.close()

    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_database()

