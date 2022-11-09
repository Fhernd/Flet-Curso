import flet
from flet import Column, ElevatedButton, Page, Text, TextField


def main(page: Page):
    txt_first_name = TextField(label='Nombre', autofocus=True)
    txt_last_name = TextField(label='Apellido')
    col_controles = Column()

    def saludar_clicked(event):
        col_controles.controls.append(Text(f'¡Hola, {txt_first_name.value} {txt_last_name.value}!'))

        txt_first_name.value = ''
        txt_last_name.value = ''

        page.update()
        txt_first_name.focus()

    btn_saludar = ElevatedButton('Saludar', on_click=saludar_clicked)

    page.add(
        txt_first_name,
        txt_last_name,
        btn_saludar,
        col_controles
    )


# Ejecución de la aplicación en modo escritorio:
flet.app(target=main)
