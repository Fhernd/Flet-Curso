import flet
from flet import ElevatedButton, Page, Text, TextField, Row


def main(page: Page):
    txt_nombre = TextField(label='Digite su nombre')

    lbl_saludo = Text()

    def saludar(event):
        lbl_saludo.value = f'¡Hola... {txt_nombre.value}!'
        page.update()

    row = Row(controls=[
        txt_nombre,
        ElevatedButton(text='Saludar', on_click=saludar),
        lbl_saludo
    ])

    page.add(row)


# Ejecución en el escritorio:
flet.app(target=main)
