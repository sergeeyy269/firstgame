import psycopg2
from psycopg2 import sql

def init_db():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT,
        user_id INTEGER UNIQUE,
        balance INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_user(username, user_id):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (username, user_id) VALUES (%s, %s)
    ON CONFLICT (user_id) DO NOTHING
    ''', (username, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_balance(user_id, amount):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users SET balance = balance + %s WHERE user_id = %s
    ''', (amount, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_balance(user_id):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    cursor = conn.cursor()
    cursor.execute('''
    SELECT balance FROM users WHERE user_id = %s
    ''', (user_id,))
    balance = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return balance
