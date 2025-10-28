import os
from dotenv import load_dotenv  
load_dotenv()
from src.constants import MONGODB_URL_KEY as MONGODB_URL

mongo_db_url = os.getenv(MONGODB_URL)
print(f"MongoDB URL: {mongo_db_url}")