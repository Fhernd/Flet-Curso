import flet
from flet import ElevatedButton, Page, Text, TextField, Row


def saludar(event):
    print('¡Hola!')


def main(page: Page):
    row = Row(controls=[
        TextField(label='Digite su nombre'),
        ElevatedButton(text='Saludar', on_click=saludar)
    ])

    page.add(row)


# Ejecución en el escritorio:
flet.app(target=main)
