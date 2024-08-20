import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

mongo_url = os.getenv('MONGODB_URL')
database = os.getenv('DATABASE')