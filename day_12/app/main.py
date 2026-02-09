#public routes:
'''
post/api/auth/register
post/api/auth/login
get/api/posts
get/api/posts/{id}
'''
#protected routes:
'''
post/api/posts
put/api/posts{id}
delete/api/posts/{id}
get/api/users/me
get/api/users/me/posts
'''
from fastapi import FastAPI, HTTPException, Depends, status,Response
from dotenv import load_dotenv
from datetime import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import load_users, save_users, load_posts, save_posts, find_post_by_id, find_user_by_username, find_user_by_email, get_next_post_id, get_next_user_id, get_post_by_author
from app.models import UserLogin, UserRegister, UserResponse, PostUpdate, PostCreate, PostResponse, Token, TokenData
from app.auth import get_hashed_password, verify_password, create_access_token, verify_access_token

load_dotenv()
app = FastAPI()
# Security scheme
security = HTTPBearer()

@app.post("/api/auth/register")
async def register(body: UserRegister):
    '''Create new user'''
    users = load_users()

    if find_user_by_username(body.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    if find_user_by_email(body.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password = get_hashed_password(body.password)
    new_user = {
        'id': get_next_user_id(),
        'username' : body.username,
        'email' : body.email,
        'full_name' : body.full_name,
        'password_hash' : hashed_password,
        'created_at' : datetime.now().isoformat()
    }

    users.append(new_user)
    save_users(users)
    
    return new_user #FastAPI will format as UserResponse

@app.post("/api/auth/login", response_model=Token)
async def login(body:UserLogin):
    '''Login user and return access token'''
    user = find_user_by_username(body.username)
    if not user or not verify_password(body.password, user['password_hash']):
         raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(user['username'])
    return {
        "access_token" : access_token, 
        "token_type": "bearer"
    }

@app.get("/api/users/me")
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    username = payload.get("sub") 
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    user = find_user_by_username(username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user

@app.get("/api/posts")
async def get__all_posts():
    posts = load_posts()
    return posts

@app.get("/api/posts/{id}")
async def get_single_post(id:int):
    return find_post_by_id(1)

@app.post("/api/posts")
async def create_post(body: PostCreate, current_user: dict = Depends(get_current_user)):
    """Create a new post (requires authentication)"""
    posts = load_posts()
    new_post = {
        "id": get_next_post_id(),
        "title" : body.title,
        "content" : body.content,
        "author_id": current_user['id'],
        "author_username" : current_user['username'],
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    posts.append(new_post)
    save_posts(posts)
    return new_post

@app.get("/api/users/me/posts")
async def get_my_post(current_user: dict = Depends(get_current_user)):
    posts = load_posts()
    my_posts = []
    user_id = current_user['id']
    for post in posts:
        if user_id == post['author_id']:
            my_posts.append(post)

    return my_posts

@app.put("/api/posts/{id}")
async def update_post(id:int,body:PostUpdate, current_user: dict = Depends(get_current_user)):
    post_to_update =find_post_by_id(id)
    if not post_to_update:
        raise HTTPException(status_code=404, detail="Post not found")
    posts = load_posts()

    if post_to_update["author_id"] != current_user['id']:
        raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not authorized to perform requested action"
    )
    all_posts = load_posts()
    for p in all_posts:
        if p["id"] == id:
            p['title'] = body.title
            p['content'] = body.content
            save_posts(all_posts)
            return p

@app.delete("/api/posts/{id}")
async def delete_post(id : int, my_post: dict = Depends(get_my_post)):
    posts = load_posts()
    for index, post in enumerate(my_post):
        if post["id"] == id:
            posts.pop(index)
            save_posts(posts)
            return Response(status_code=status.HTTP_204_NO_CONTENT)      
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id: {id} does not exist"
    )      
