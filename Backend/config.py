import os
from dotenv import load_dotenv

load_dotenv()
print("Loaded DB:", os.getenv("DATABASE_URL")) 

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False