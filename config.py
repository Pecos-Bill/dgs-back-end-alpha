import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Grab the DATABASE_URL from env variables
    database_url = os.getenv("DATABASE_URL")

    # Fix common Heroku issue (if the URL starts with postgres://)
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key")