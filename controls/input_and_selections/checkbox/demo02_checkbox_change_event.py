import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Checkbox change event'

    def chk_changed(event):
        lbl_estado.value = f'El estado ha cambiado a {chk_control.value}'

        page.update()
    

    chk_control = Checkbox(label="Checkbox with 'change' event", on_change=chk_changed)
    lbl_estado = Text()

    page.add(
        chk_control,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
