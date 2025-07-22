import sqlite3

DB_FILE = "CharityLink-Updated.db"

def get_connection():
    """Create a new database connection."""
    return sqlite3.connect(DB_FILE)

def create_user(email, password, name, role="User"):
    """Register a new user. Role defaults to 'User'."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (email, password, name, role) VALUES (?, ?, ?, ?)",
            (email, password, name, role)
        )
        conn.commit()

def get_user_by_email(email):
    """Fetch a user row by email. Returns dict or None."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, email, password, name, role FROM users WHERE email = ?",
            (email,)
        )
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "email": row[1],
                "password": row[2],
                "name": row[3],
                "role": row[4]
            }
        return None

def validate_login(email, password):
    """Checks email/password; returns user dict or None."""
    user = get_user_by_email(email)
    if user and user["password"] == password:
        return user
    return None

def get_all_users():
    """Returns all users except passwords (for admin dashboard)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, email, name, role FROM users"
        )
        return cursor.fetchall()

# Optionally: add a get_user_by_id if you need to fetch a user with just the ID.
def get_user_by_id(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, email, name, role FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "email": row[1],
                "name": row[2],
                "role": row[3]
            }
        return None
