from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserRegister(BaseModel):
    """Data for user registration"""
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    """Data for user login"""
    username: str
    password: str

class UserResponse(BaseModel):
    """User data returned to client (no password!)"""
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    created_at: datetime

class Token(BaseModel):
    """Token response"""
    access_token : str
    token_type : str

class TokenData(BaseModel):
    """Data extracted from token"""
    username : Optional[str] = None

class PostCreate(BaseModel):
    """Data for creating a post"""
    title: str = Field(..., min_length=10, max_length=200)
    content: str = Field(..., min_length=10)

class PostUpdate(BaseModel):
    """Data for updating a post"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)

class PostResponse(BaseModel):
    """Post data returned to client"""
    id: int
    title: str
    content: str
    author_id: int
    author_username: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    sentiment: str
    sentiment_score: float

class SentimentAnalysis(BaseModel):
    """Sentiment analysis result"""
    sentiment : str
    score : float

class AnalyzeRequest(BaseModel):
    """Request to analyze text"""
    text : str = Field(..., min_length=10)