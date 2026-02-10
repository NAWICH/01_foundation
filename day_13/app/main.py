# API Routes:
# public routes:
# post/api/auth/register
# post/api/auth/login
# get/api/posts
# get/api/posts/{id}
#
# protected routes:
# post/api/posts
# put/api/posts{id}
# delete/api/posts/{id}
# get/api/users/me
# get/api/users/me/posts

from fastapi import FastAPI, HTTPException, Depends, status, Response
from dotenv import load_dotenv
from datetime import datetime
from app.database import load_posts, save_posts, find_post_by_id
from app.models import UserLogin, UserRegister, PostUpdate, PostCreate, Token
from app.auth import get_current_user

load_dotenv()
app = FastAPI()

@app.post("/api/auth/register")
async def register(body: UserRegister):
    """Create new user"""
    from app.database import load_users, save_users, find_user_by_username, find_user_by_email
    from app.auth import get_hashed_password
    
    users = load_users()

    if find_user_by_username(body.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    if find_user_by_email(body.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password = get_hashed_password(body.password)
    new_user = {
        'username' : body.username,
        'email' : body.email,
        'full_name' : body.full_name,
        'password_hash' : hashed_password,
        'created_at' : datetime.now().isoformat()
    }
    save_users(new_user)
    
    return new_user

@app.post("/api/auth/login", response_model=Token)
async def login(body: UserLogin):
    """Login user and return access token"""
    from app.database import find_user_by_username
    from app.auth import verify_password, create_access_token
    
    user = find_user_by_username(body.username)
    if not user or not verify_password(body.password, user['password_hash']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(user['username'])
    return {
        "access_token" : access_token, 
        "token_type": "bearer"
    }

@app.get("/api/users/me")
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    """Get current authenticated user info"""
    return current_user

@app.get("/api/posts")
async def get_all_posts():
    """Get all posts"""
    posts = load_posts()
    return posts

@app.get("/api/posts/{id}")
async def get_single_post(id: int):
    """Get a single post by ID"""
    post = find_post_by_id(id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/api/posts")
async def create_post(body: PostCreate, current_user: dict = Depends(get_current_user)):
    """Create a new post (requires authentication)"""
    from app.database import load_posts, save_posts
    
    posts = load_posts()
    new_post = {
        "title" : body.title,
        "content" : body.content,
        "author_id": current_user['id'],
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    posts.append(new_post)
    save_posts(posts)
    return new_post

@app.get("/api/users/me/posts")
async def get_my_posts(current_user: dict = Depends(get_current_user)):
    """Get posts by current authenticated user"""
    from app.database import load_posts
    
    posts = load_posts()
    my_posts = []
    user_id = current_user['id']
    for post in posts:
        if user_id == post['author_id']:
            my_posts.append(post)

    return my_posts

@app.put("/api/posts/{id}")
async def update_post(id: int, body: PostUpdate, current_user: dict = Depends(get_current_user)):
    """Update a post (requires authentication)"""
    from app.database import load_posts, save_posts, find_post_by_id
    
    post_to_update = find_post_by_id(id)
    if not post_to_update:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if post_to_update["author_id"] != current_user['id']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform requested action"
        )
    
    posts = load_posts()
    for p in posts:
        if p["id"] == id:
            if body.title is not None:
                p['title'] = body.title
            if body.content is not None:
                p['content'] = body.content
            p['updated_at'] = datetime.now().isoformat()
            save_posts(posts)
            return p

@app.delete("/api/posts/{id}")
async def delete_post(id: int, current_user: dict = Depends(get_current_user)):
    """Delete a post (requires authentication)"""
    from app.database import load_posts, save_posts, find_post_by_id
    
    post_to_delete = find_post_by_id(id)
    if not post_to_delete:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if post_to_delete["author_id"] != current_user['id']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform requested action"
        )
    
    posts = load_posts()
    for index, post in enumerate(posts):
        if post["id"] == id:
            posts.pop(index)
            save_posts(posts)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id: {id} does not exist"
    )

