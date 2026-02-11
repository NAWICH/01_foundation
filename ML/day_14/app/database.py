import sqlite3

def create_connection():
    """Create database connection"""
    connection = sqlite3.connect("./database.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    """Create database tables"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   full_name TEXT,
                   password_hash TEXT NOT NULL,
                   created_at TEXT NOT NULL)""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            sentiment Text NOT NULL,
            sentiment_score REAL NOT NULL,
            FOREIGN KEY (author_id) REFERENCES user(id)
        )
    """)
    connection.commit()
    connection.close()

def load_users(): 
    """Load users from database"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    connection.close()

    users = [dict(row) for row in rows]
    return users

def save_users(users):
    """Save a single user to database"""
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user(username, email, full_name, password_hash, created_at) VALUES(?,?,?,?,?)",
                      (users['username'], users['email'], users['full_name'], users['password_hash'], users['created_at']))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print(f"Error saving user {e}")
        return False

def load_posts():
    """Load all posts from database"""
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM post")
        rows = cursor.fetchall()
        connection.close()

        posts = [dict(row) for row in rows]
        return posts
    except Exception as e :
        print(f"error : {e}")
        return []

def save_posts(posts):
    """Save a single post to database"""
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO post(title, content, author_id, created_at, updated_at, sentiment, sentiment_score) VALUES(?,?,?,?,?,?,?)""",
                      (posts['title'], posts['content'], posts['author_id'], posts['created_at'], posts['updated_at'], posts['sentiment'], posts['sentiment_score']))
        connection.commit()
        post_id = cursor.lastrowid
        connection.close()
        return post_id
    except Exception as e :
        print(f"Error saving posts : {e}")
        return False
    
def find_user_by_username(username: str):
    """Find user by username"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    row = cursor.fetchone()
    connection.close()

    if row:
        return dict(row)  
    return None
    
def find_user_by_email(email: str):
    """Find user by email"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE email=?", (email,))
    row = cursor.fetchone()
    connection.close()

    if row:
        return dict(row)  
    return None

def find_post_by_id(post_id: int):
    """Find post by ID"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM post WHERE id=?", (post_id,))
    row = cursor.fetchone()
    connection.close()
    
    if row:
        return dict(row)
    return None

def get_post_by_sentiment(sentiment:str):
    """get post by sentiment"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM post where sentiment_label =?", (sentiment,))
    rows= cursor.fetchall()
    connection.close()
    
    posts = [dict(row) for row in rows]
    return posts
# Initialize database tables
create_table()
