import flet
from flet import ElevatedButton, Page, Row, Text, UserControl


class CounterControl(UserControl):
    def increment(self, event):
        self.counter += 1
        self.lbl_counter.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0

        self.lbl_counter = Text("0")
        btn_increment = ElevatedButton("Incrementar", on_click=self.increment)

        return Row([self.lbl_counter, btn_increment])


def main(page: Page):
    page.title = "Contadores"

    page.add(CounterControl())
    page.add(CounterControl())


if __name__ == "__main__":
    flet.app(target=main)
