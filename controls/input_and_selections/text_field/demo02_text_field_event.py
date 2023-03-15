import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Text Field event"

    def txt_changed(event):
        lbl_estado.value = event.control.value 

        page.update()

    
    lbl_estado = Text()

    txt_1 = TextField(label="Textbox with 'change' event:", on_change=txt_changed)

    page.add(
        txt_1,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
