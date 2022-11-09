import flet
from flet import Column, ElevatedButton, Page, Text, TextField
from flet.ref import Ref


def main(page: Page):
    txt_first_name = Ref[TextField]()
    txt_last_name = Ref[TextField]()
    col_controles = Ref[Column]()

    def saludar_clicked(event):
        col_controles.current.controls.append(Text(f'¡Hola, {txt_first_name.current.value} {txt_last_name.current.value}!'))

        txt_first_name.current.value = ''
        txt_last_name.current.value = ''

        page.update()
        txt_first_name.current.focus()

    btn_saludar = ElevatedButton('Saludar', on_click=saludar_clicked)

    page.add(
        TextField(ref=txt_first_name, label='Nombre', autofocus=True),
        TextField(ref=txt_last_name, label='Apellido'),
        btn_saludar,
        Column(ref=col_controles)
    )


# Ejecución de la aplicación en modo escritorio:
flet.app(target=main)
