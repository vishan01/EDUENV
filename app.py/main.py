import webbrowser

from taipy.gui import Gui, Markdown, notify, Html
import login
import dashboard

value = 0
logo = "./images/Homepage.png"


page1 = Html("app.py/index.html")


def image_action(state):
    webbrowser.open(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")


def on_push(state):
    ...


def on_slider(state):
    if state.value == 100:
        notify(state, "success", "Taipy is running!")


def on_change(state, var_name: str, var_value):
    ...


page = {
    "home": page1
}

if __name__ == "__main__":
    gui = Gui(pages=page, css_file="/styles.css")
    gui.add_page(name="login", page=login.page)
    gui.run(title="EDUENV")
