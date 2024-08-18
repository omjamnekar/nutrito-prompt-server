from dotenv import load_dotenv
from pymongo import MongoClient
import os


load_dotenv()
client = MongoClient(os.getenv("MONGO_USER_KEY"))
db = client["Nutrito"]  
collection = db["users"]  

def get_user(username):
    return collection.find_one({"username": username})

def validate_user(username, password):
    user = get_user(username)
    if user and user['password'] == password:
        return True
    return False


# EXMAPLE FOR TESTING MONGO CLIENT
# ////////////////////////////////////////////////////////////////
# #  usage:
# username_to_search = "Shiva"  
# password_to_validate = "12345678"  

# get_user(username_to_search)

# if validate_user(username_to_search, password_to_validate):
#     print("User credentials are valid.")
# else:
#     print("Invalid credentials.")
