from taipy.gui import Gui, Html, notify, navigate
import dashboard

Username = ""
Password = ""
page = Html(
    """
    <center>
        <h2>Welcome to the Login Page</h2>
        <p>Username</p>
        <taipy:input>{Username}</taipy:input>
        <p>Password</p>
        <taipy:input>{Password}</taipy:input>
        <taipy:button on_action="submit">Submit</taipy:button>

    </center>
"""
)


def submit(state):
    navigate(state, to=dashboard.page)
