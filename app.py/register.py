from taipy.gui import Html, navigate
from pymongo import MongoClient
import url
client = MongoClient(url.url)
db = client["users"]
collection = db["user_password"]

username = ""
value = ""
password = ""
password1 = ""
page = Html("app.py/register.html")


def Sign_up(state):
    collection.insert_one(
        {'type': state.value, 'user': state.username, 'password': state.password})
    if (state.value == "student"):
        navigate(state, to="dashboard", force=True)
    else:
        navigate(state, to="dashboard1", force=True)
