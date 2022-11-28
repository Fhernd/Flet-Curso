import flet
from flet import Column, ElevatedButton, Page, TextField, UserControl


class GreeterControl(UserControl):
    def build(self):
        txt_nombre = TextField(label="Nombre")
        btn_saludar = ElevatedButton("Saludar")

        return Column(
            [
                txt_nombre,
                btn_saludar,
            ]
        )


def main(page: Page):
    page.title = "User Control"

    page.add(GreeterControl())


if __name__ == "__main__":
    flet.app(target=main)
