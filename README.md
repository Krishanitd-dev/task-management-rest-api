Install:

pip install python-dotenv

Create:

from dotenv import load_dotenv
import os

load_dotenv()

database_name = os.getenv("tasks.db")