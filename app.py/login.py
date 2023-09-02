from taipy.gui import Gui, Markdown, notify, navigate
import dashboard

Username = ""
Password = ""
page = Markdown(
    """
<center>
<center> Welcome to Login</center>
USERNAME
<|{Username}|input|>
PASSWORD
<|{Password}|input|password=True|>
</center>
<|Submit|button|on_action=submit|>
"""
)


def submit(state):
    navigate(state, "https://taipy.io")


gui = Gui(page=page)
