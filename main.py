
import sqlite3
import re
import hashlib

DB_NAME = "security_demo.db"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        ("student",)
    )

    if cursor.fetchone() is None:
        password_hash = hashlib.sha256(
            "demo123".encode()
        ).hexdigest()

        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("student", password_hash)
        )

    conn.commit()
    conn.close()


def detect_suspicious_input(value):
    patterns = [
        r"'\s*OR\s+'?\w+'?\s*=\s*'?\w+",
        r"\bUNION\s+SELECT\b",
        r"\bDROP\s+TABLE\b",
        r"--",
        r"/\*.*?\*/"
    ]

    for pattern in patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return True

    return False


def login(username, password):
    if detect_suspicious_input(username) or detect_suspicious_input(password):
        print("\nWarning: Suspicious input detected.")
        print("Login rejected for this security demo.")
        return

    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Parameterized query helps prevent SQL injection.
    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password_hash = ?",
        (username, password_hash)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        print("\nLogin successful!")
    else:
        print("\nInvalid username or password.")


def main():
    setup_database()

    print("=== SQL Injection Detection Demo ===")
    print("Demo account: student")
    print("Demo password: demo123")

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    login(username, password)


if __name__ == "__main__":
    main()
