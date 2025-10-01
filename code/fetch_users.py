import sqlite3


def create_user_table(db_path):
    """
    Erstellt die Tabelle 'users' in der Datenbank, falls sie nicht existiert.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def get_user(db_path, user_id):
    """
    Fetch a user from the database by user_id.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def add_sample_users(db_path):
    users = [
        (1, "alice", "alice@example.com"),
        (2, "bob", "bob@example.com"),
        (3, "carol", "carol@example.com")
    ]
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO users (id, username, email) VALUES (?, ?, ?)", users)
    conn.commit()
    conn.close()


# create_user_table("users.db")
# add_sample_users("users.db")

print(get_user("users.db", "1; DROP TABLE users;"))  # SQL Injection Example


# get_user("users.db", 1)
