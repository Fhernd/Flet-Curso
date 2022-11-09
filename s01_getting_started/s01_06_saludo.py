import flet
from flet import ElevatedButton, Page, Text, TextField, Row


def main(page: Page):
    txt_nombre = TextField(label='Digite su nombre')

    def saludar(event):
        print(f'¡Hola... {txt_nombre.value}!')

    row = Row(controls=[
        txt_nombre,
        ElevatedButton(text='Saludar', on_click=saludar)
    ])

    page.add(row)


# Ejecución en el escritorio:
flet.app(target=main)
