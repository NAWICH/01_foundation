# 🤖 ML-Powered Blog API

A RESTful API for a blogging platform with **AI-powered sentiment analysis** using machine learning. Built with FastAPI, SQLite, and Hugging Face Transformers.

## ✨ Features

### Core Features
- 🔐 **User Authentication** - JWT token-based auth with bcrypt password hashing
- 📝 **Blog Posts** - Create, read, update, delete blog posts
- 👤 **User Management** - Register, login, view profile
- 🔒 **Authorization** - Users can only edit/delete their own posts

### AI Features (Day 14)
- 🤖 **Sentiment Analysis** - Automatic sentiment detection on all posts
- 📊 **Sentiment Filtering** - Filter posts by sentiment (positive/negative/neutral)
- 🎯 **ML API Endpoint** - Analyze sentiment of any text
- 🚀 **Hugging Face Integration** - State-of-the-art multilingual sentiment model

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite
- **Authentication:** JWT (python-jose) + bcrypt
- **ML Model:** Hugging Face Transformers (tabularisai/multilingual-sentiment-analysis)
- **Validation:** Pydantic
- **Environment:** python-dotenv

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- 2GB free disk space (for ML model)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/NAWICH/01_foundation.git
cd 01_foundation/day_14_ml_api
```

### 2. Create virtual environment

```bash
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
JWT_SECRET_KEY=your-super-secret-key-here-change-in-production
JWT_ALGORITHM=HS256
TOKEN_EXPIRY_MINUTES=60
```

**Generate a secure secret key:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 5. Run the application

```bash
# Development mode (with auto-reload)
fastapi dev app/main.py

# Or using uvicorn
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

### 6. Access API Documentation

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📚 API Endpoints

### Authentication

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "created_at": "2026-02-10T12:00:00"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Response:** `200 OK`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### User Endpoints

#### Get Current User
```http
GET /api/users/me
Authorization: Bearer <token>
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "created_at": "2026-02-10T12:00:00"
}
```

### Blog Post Endpoints

#### Get All Posts
```http
GET /api/posts
# Optional: Filter by sentiment
GET /api/posts?sentiment=positive
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Amazing Day!",
    "content": "Today was absolutely fantastic!",
    "author_id": 1,
    "sentiment": "POSITIVE",
    "sentiment_score": 0.9987,
    "created_at": "2026-02-10T14:30:00",
    "updated_at": "2026-02-10T14:30:00"
  }
]
```

#### Get Single Post
```http
GET /api/posts/{id}
```

#### Create Post (Protected)
```http
POST /api/posts
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "My First Blog Post",
  "content": "This is an amazing experience learning AI!"
}
```

**Response:** `201 Created`
```json
{
  "id": 2,
  "title": "My First Blog Post",
  "content": "This is an amazing experience learning AI!",
  "author_id": 1,
  "sentiment": "POSITIVE",
  "sentiment_score": 0.9845,
  "created_at": "2026-02-10T15:00:00",
  "updated_at": "2026-02-10T15:00:00"
}
```

**Note:** Sentiment is automatically analyzed when creating posts!

#### Update Post (Protected)
```http
PUT /api/posts/{id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "content": "Updated content"
}
```

#### Delete Post (Protected)
```http
DELETE /api/posts/{id}
Authorization: Bearer <token>
```

**Response:** `204 No Content`

### ML Sentiment Analysis

#### Analyze Any Text
```http
POST /api/analyze
Content-Type: application/json

{
  "text": "This is absolutely wonderful!"
}
```

**Response:** `200 OK`
```json
{
  "sentiment": "POSITIVE",
  "score": 0.9998
}
```

**Sentiment Labels:**
- `POSITIVE` - Positive sentiment detected
- `NEGATIVE` - Negative sentiment detected
- `NEUTRAL` - Neutral sentiment detected

**Score:** Confidence score between 0 and 1 (higher = more confident)

## 🧪 Testing

### Using FastAPI Docs (Easiest)

1. Go to http://localhost:8000/docs
2. Click "Authorize" button (top right)
3. Login to get token, paste in authorization dialog
4. Test all endpoints interactively

### Using cURL

```bash
# Register
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
  }'

# Login (save the token)
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "password123"
  }'

# Create post (use your token)
curl -X POST http://localhost:8000/api/posts \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Post",
    "content": "This is a fantastic test post!"
  }'

# Analyze sentiment
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I love this so much!"
  }'

# Get posts filtered by sentiment
curl http://localhost:8000/api/posts?sentiment=positive
```

## 📁 Project Structure

```
day_14_ml_api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app and all routes
│   ├── models.py         # Pydantic models for validation
│   ├── database.py       # SQLite database operations
│   ├── auth.py           # Authentication (JWT, bcrypt)
│   └── ml_service.py     # ML sentiment analysis service
│
├── database.db           # SQLite database (created automatically)
├── .env                  # Environment variables (not in git)
├── .env.example          # Template for .env
├── .gitignore           # Git ignore file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔒 Security Features

- **Password Hashing:** bcrypt with salt
- **JWT Tokens:** Secure token-based authentication
- **Token Expiration:** Tokens expire after 60 minutes
- **Authorization Checks:** Users can only modify their own posts
- **SQL Injection Prevention:** Parameterized queries
- **Input Validation:** Pydantic models validate all inputs

## 🤖 ML Model Details

**Model:** tabularisai/multilingual-sentiment-analysis

**Features:**
- Multilingual support (English, Spanish, French, German, Italian, Portuguese)
- State-of-the-art transformer architecture
- High accuracy sentiment classification
- Returns sentiment label + confidence score

**First Run:**
- Model downloads automatically (~500MB)
- Takes 2-3 minutes on first run
- Cached locally for future runs
- Subsequent loads take ~5 seconds

## 🌟 Key Learning Outcomes

This project demonstrates:

1. **REST API Development** - Building production-ready APIs with FastAPI
2. **Database Design** - Relational database with SQLite
3. **Authentication & Security** - JWT tokens, password hashing, authorization
4. **ML Integration** - Serving machine learning models via API
5. **Natural Language Processing** - Sentiment analysis with transformers
6. **API Documentation** - Auto-generated docs with OpenAPI/Swagger
7. **Project Structure** - Professional code organization
8. **Error Handling** - Proper HTTP status codes and error messages

## 📊 Example Use Cases

**1. Content Moderation**
- Automatically flag negative posts for review
- Filter toxic content

**2. User Insights**
- Track user sentiment over time
- Identify happy vs unhappy users

**3. Content Curation**
- Show positive content first
- Recommend uplifting posts

**4. Analytics Dashboard**
- Sentiment trends
- Popular topics by sentiment

## 🚀 Future Enhancements

Potential improvements:

- [ ] Pagination for post listings
- [ ] Search functionality
- [ ] Post comments with sentiment
- [ ] User follower system
- [ ] Real-time sentiment dashboard
- [ ] Multi-language support
- [ ] Emotion detection (joy, anger, sadness, etc.)
- [ ] PostgreSQL for production
- [ ] Redis caching for ML results
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Comprehensive test suite

## 🐛 Common Issues

### Issue: Model download fails
**Solution:** Check internet connection. Model is ~500MB and requires stable connection.

### Issue: "Failed to create post"
**Solution:** Delete `database.db` and restart server to recreate schema with sentiment columns.

### Issue: Token expired
**Solution:** Login again to get a new token. Tokens expire after 60 minutes.

### Issue: Slow first request
**Solution:** This is normal. First ML inference loads the model (~5 seconds). Subsequent requests are fast.

## 📖 Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [JWT Introduction](https://jwt.io/introduction)

## 👨‍💻 Development Journey

**Days 1-10:** Python fundamentals, file handling, API basics  
**Days 11-12:** REST API development, authentication  
**Day 13:** Database integration with SQLite  
**Day 14:** ML model integration with Hugging Face 🎉

**Repository:** https://github.com/NAWICH/01_foundation

## 🤝 Contributing

This is a learning project, but feedback and suggestions are welcome!

## 📝 License

This project is for educational purposes.

## 🙏 Acknowledgments

- FastAPI for the amazing web framework
- Hugging Face for transformer models
- tabularisai for the multilingual sentiment model
- AgenticAiLabs AI Engineering Roadmap

---

**Built with ❤️ while learning AI Engineering**

*Part of a 30-day intensive journey to become an AI Engineer*

**Next Steps:** Deep Learning, LLMs, RAG Systems, and Building Production AI Applications

---

## 📧 Contact

**Developer:** Nawich  
**GitHub:** https://github.com/NAWICH  
**Project:** Day 14 of AI Engineering Bootcamp  
**Date:** February 2026