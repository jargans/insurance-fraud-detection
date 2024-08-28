import mysql.connector
import os

def init_db():
    db_config = {
        'host': os.getenv('MYSQL_HOST', 'localhost'),
        'user': os.getenv('MYSQL_USER', 'flaskuser'),
        'password': os.getenv('MYSQL_ROOT_PASSWORD', 'password'),
        'password': os.getenv('MYSQL_PASSWORD', 'password'),
        'database': os.getenv('MYSQL_DATABASE', 'flaskapp'),
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create tables if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
