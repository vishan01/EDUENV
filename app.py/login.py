from taipy.gui import Gui, Html, notify, navigate
import dashboard
from pymongo import MongoClient
import url

client = MongoClient(
    host=url.url)
db = client["users"]
collection = db["user_password"]
Username = ""
Password = ""
page = Html("app.py/login.html")


def submit(state):
    details = collection.find_one({"user": state.Username})
    if (details == None):
        details = {"user": " "*100, "password": " "*100}
    if (state.Username == details["user"] and state.Password == details["password"]):
        if (details["type"] == "student"):
            navigate(state, to="dashboard", force=True)
        else:
            navigate(state, to="dashboard1", force=True)
    else:
        navigate(state, to="login", force=True)
