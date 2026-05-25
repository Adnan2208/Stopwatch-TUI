from textual.app import App
from textual.widgets import Header,Footer,Static,Button
from textual.containers import ScrollableContainer

class StopwatchTime(Static):
    pass


# Creating a custom widget:
class CustomStopwatchWidget(Static):
    # Static is similar to a div (Inherit it to build a custom widget)
    def compose(self):
        yield Button("Start",variant="success")
        yield Button("Stop",variant="error")
        yield Button("Reset")
        yield StopwatchTime("00:00:00.00")


class Stopwatch(App):
    # BINDINGS, takes an array of tuples which represent the key bindings of the tui
    BINDINGS = [
        ("d","toggleDarkMode","This is a method that is used to toggle dark and light modes")
    ]

    CSS_PATH = "stopwatch.tcss"

    def compose(self):
        yield Header()
        yield Footer()
        # This will put the CustomStopWatchWidget inside the container so that we can get auto scrollbars and handle them together.
        with ScrollableContainer(id="stopwatches"):
            yield CustomStopwatchWidget()
            yield CustomStopwatchWidget()

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
