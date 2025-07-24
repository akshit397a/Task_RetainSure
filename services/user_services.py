from db.connection import get_connection
from utils.hashing import hash_password, verify_password
from utils.validation import is_valid_username, is_valid_password

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(data):
    username = data.get("username")
    password = data.get("password")

    if not (is_valid_username(username) and is_valid_password(password)):
        return {"error": "Invalid username or password"}, 400

    hashed_pw = hash_password(password)
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        return {"message": "User created successfully"}, 201
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        conn.close()

def update_user(user_id, data):
    username = data.get("username")
    password = data.get("password")

    if not username and not password:
        return {"error": "No update fields provided"}, 400

    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    values = []

    if username:
        if not is_valid_username(username):
            return {"error": "Invalid username"}, 400
        updates.append("username = ?")
        values.append(username)

    if password:
        if not is_valid_password(password):
            return {"error": "Invalid password"}, 400
        updates.append("password = ?")
        values.append(hash_password(password))

    values.append(user_id)
    try:
        cursor.execute(f"UPDATE users SET {', '.join(updates)} WHERE id = ?", values)
        conn.commit()
        return {"message": "User updated successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return {"message": "User deleted successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        conn.close()

def search_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    conn.close()
    return results

def login_user(data):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Missing credentials"}, 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and verify_password(password, user[0]):
        return {"message": "Login successful"}, 200
    else:
        return {"error": "Invalid credentials"}, 401
