import flet
from flet import ElevatedButton, Page, Row, Text, UserControl


class CounterControl(UserControl):
    def __init__(self, initial_value=0):
        super().__init__()
        self.counter = initial_value

    def increment(self, event):
        self.counter += 1
        self.lbl_counter.value = str(self.counter)
        self.update()

    def build(self):

        self.lbl_counter = Text(str(self.counter))
        btn_increment = ElevatedButton("Incrementar", on_click=self.increment)

        return Row([self.lbl_counter, btn_increment])


def main(page: Page):
    page.title = "Contadores"

    page.add(CounterControl())
    page.add(CounterControl(10))


if __name__ == "__main__":
    flet.app(target=main)
