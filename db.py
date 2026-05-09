import sqlite3
from datetime import datetime

DB_PATH = "bot.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        first_name TEXT,
        command TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def log_user(user, command=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_logs (user_id, username, first_name, command, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user.id,
        user.username,
        user.first_name,
        command,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
