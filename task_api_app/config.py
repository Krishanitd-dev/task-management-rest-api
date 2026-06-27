from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME", "tasks.db")
APP_NAME = os.getenv("APP_NAME", "My Task API")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
