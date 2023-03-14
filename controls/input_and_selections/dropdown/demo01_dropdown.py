import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Dropdown'

    def btn_clicked(event):
        lbl_estado.value = f'Valor del dropdown: {dbx.value}'

        page.update()
    

    lbl_estado = Text()
    
    btn = ElevatedButton(text='Submit', on_click=btn_clicked)

    dbx = Dropdown(
        width=200,
        options=[
            flt.dropdown.Option('Red'),
            flt.dropdown.Option('Green'),
            flt.dropdown.Option('Blue'),
        ])
    
    page.add(
        dbx,
        btn,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
