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
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from datetime import datetime
from app.database import load_users, save_users, load_posts, save_posts, find_post_by_id, find_user_by_username, find_user_by_email, get_next_post_id, get_next_user_id, get_post_by_author
from app.models import UserLogin, UserRegister, UserResponse, PostUpdate, PostCreate, PostResponse, Token, TokenData
from app.auth import get_hashed_password, verify_password, create_access_token, verify_access_token

load_dotenv()
app = FastAPI()

#public
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

@app.post("/api/auth/login")
async def login():
    pass

@app.get("api/posts")
async def get__all_posts():
    pass

@app.get("api/posts/{id}")
async def get_single_post(id):
    pass

#protected
@app.post("api/posts")
async def create_post():
    pass

@app.put("api/posts/{id}")
async def update_post(id):
    pass

@app.delete("api/posts/{id}")
async def delete_post(id):
    pass

@app.get("api/users/me")
async def get_my_data():
    pass

@app.get("api/users/me/posts")
async def get_my_post():
    pass