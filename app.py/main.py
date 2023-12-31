import webbrowser

from taipy.gui import Gui, Markdown, notify, Html, navigate
import login
import dashboard
import dashboard1
import register

value = " ©2023 EduEnv. All rights reserved.\n Disclaimer: This website is for informational purposes only and does not constitute professional educational advice.\nConsult with a qualified educator or institution for personalized guidance."
logo = "./images/logo.png"
icon = "./images/ICON.png"

page1 = Html("app.py/index.html")


def image_action(state):
    webbrowser.open(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")


def logins(state):
    navigate(state, to="login")


def image_click(state):
    navigate(state, to="home", force=True)


page = {
    "home": page1
}


if __name__ == "__main__":
    gui = Gui(pages=page)
    gui.add_page(name="login", page=login.page)
    gui.add_page(name="register", page=register.page)
    gui.add_page(name="dashboard", page=dashboard.page)
    gui.add_page(name="dashboard1", page=dashboard1.page)
    gui.run(title="EDUENV", watermark=" ", favicon=icon)
