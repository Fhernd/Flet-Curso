import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Dropdown change'

    def dbx_changed(event):
        lbl_estado.value = f'Valor actual del dropdown: {dbx.value}'
        page.update()
    
    lbl_estado = Text()

    dbx = Dropdown(
        on_change=dbx_changed,
        options=[
            flt.dropdown.Option('Red'),
            flt.dropdown.Option('Green'),
            flt.dropdown.Option('Blue'),
        ],
        width=200
    )

    page.add(
        dbx,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
