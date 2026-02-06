#authentication logic
#Load users from Json
#Load Posts from Json
#save users to json
#save post to Json
#Find user by username/email
#Find post by ID
#Get posts by author
import os
import json

USER_FILE = "./data/users.json"
POSTS_FILE = "./data/posts.json"
def load_users(): 
    """Load users from JSON file"""
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e :
        print(f"Error loading users : {e}")
        return []

def save_users(users):
    try:
        with open(USER_FILE, 'w') as f:
            json.dump(users, f, indent=2)
        return True
    except Exception as e :
        print(f"Error saving users : {e}")
        return False
    
def load_posts():
    """Save users to JSON file"""
    try:
        with open(POSTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e :
        print(f"error : {e}")
        return []

def save_posts(posts):
    """Save posts to JSON file"""
    try:
        with open("./data/posts.json", 'w') as f:
            json.dump(posts, f, indent=4)
        return True
    except Exception as e :
        print(f"Error saving posts : {e}")
        return False
    
def find_user_by_username(username: str):
    """Find user by username"""
    users = load_users()
    for user in users:
        if user['username'] == username:
            return user
            
    return None
    
def find_user_by_email(email: str):
    """Find user by email"""
    users = load_users()
    for user in users:
        if user['email'] == email:
            return user
    return None

def find_post_by_id(post_id: int):
    """Find post by ID"""
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None

def get_post_by_author(author_id: int):
    """Get all posts by author"""
    posts = load_posts()
    return [post for post in posts if post['author_id'] == author_id]

def get_next_user_id():
    """Get next available user ID"""
    users = load_users()
    if not users:
        return 1
    return max(user['id'] for user in users) + 1

def get_next_post_id():
    """Get next available post ID"""
    posts = load_posts()
    if not posts:
        return 1
    return max(post['id'] for post in posts) + 1