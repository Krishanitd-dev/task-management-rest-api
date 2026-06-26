Task API (FastAPI Project)

A simple Task Management REST API built using FastAPI and SQLite. 
Client → Routes → Services → Database → SQLite

Features

- Create tasks
- Read all tasks
- Update tasks
- Delete tasks
- Health check endpoint
- Version endpoint
- Statistics endpoint (total, completed, pending tasks)

installation 
git clone <your-repo-url> 
cd task_api

# Venv
python -m venv venv
source venv/bin/activate   # Windows

# dependancies
pip install fastapi uvicorn python-dotenv

pip install -r requirements.txt
pip install python-dotenv


database 
Create a `.env` file:
DATABASE_NAME=tasks.db
Load it in Python:

Run 
uvicorn main:app --reload