import sqlite3

def connect_db():
    """Connect to the database and create the users table if it doesn't exist."""
    conn = sqlite3.connect('Systemdb.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Create the users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        password TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()

def insert_user(username, password):
    """Insert a new user into the users table."""
    try:
        conn = sqlite3.connect('Systemdb.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (username, password))
        conn.commit()  # Commit the changes to save the new user
        print("User inserted successfully.")  # Confirm data insertion
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    finally:
        conn.close()  # Ensure the connection is closed