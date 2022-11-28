import flet
from flet import Page, Text, UserControl


class GreeterControl(UserControl):
    def build(self):
        lbl_saludo = Text("Hello world!")

        return lbl_saludo


def main(page: Page):
    page.title = "User Control"

    page.add(GreeterControl())


if __name__ == "__main__":
    flet.app(target=main)
