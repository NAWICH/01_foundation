#data validation
#hash password
#verify password
#create token
#verify token
#get current user from token
import os
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
TOKEN_EXPIRY_MINUTES = int(os.getenv("TOKEN_EXPIRY_MINUTES", "60"))
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """Hash a password"""
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    """Verify password against hash"""
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: str, expires_delta: timedelta=None):
    """Create JWT access token"""
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRY_MINUTES)

    to_encode = {"exp": expires, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY)
    return encoded_jwt

def verify_access_token(token: str):
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token,  
        JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        return payload
    except JWTError:
        return None
    
