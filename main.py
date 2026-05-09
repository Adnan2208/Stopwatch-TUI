from textual.app import App
from textual.widgets import Header,Footer

class Stopwatch(App):
    # BINDINGS, takes an array of tuples which represent the key bindings of the tui
    BINDINGS = [
        ("d","toggleDarkMode","This is a method that is used to toggle dark and light modes")
    ]

    def compose(self):
        yield Header()
        yield Footer()

    # You need to specify action_ while creating action function.
    # You can omit the action_ prefix while mentioning them in the BINDINGS
    def action_toggleDarkMode(self):
        if(self.theme == "textual-dark"):
            self.theme = ("textual-light")
        else:
            self.theme = ("textual-dark")

if __name__ == "__main__":
    stopwatchObject = Stopwatch()
    stopwatchObject.run()
