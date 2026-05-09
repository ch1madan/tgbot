import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB", "botdb"),
    "user": os.getenv("POSTGRES_USER", "bot"),
    "password": os.getenv("POSTGRES_PASSWORD", "botpass"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
}


def get_conn():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_logs (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            username TEXT,
            first_name TEXT,
            command TEXT,
            timestamp TIMESTAMP DEFAULT NOW()
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def log_user(user, command=None):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_logs (user_id, username, first_name, command, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        user.id,
        user.username,
        user.first_name,
        command,
        datetime.utcnow()
    ))

    conn.commit()
    cur.close()
    conn.close()