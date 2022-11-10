import flet
from flet import IconButton, Page, Row, TextField, icons


def main(page: Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    txt_numero = TextField(value='0', text_align='right', width=100)

    def reducir_clicked(event):
        txt_numero.value = int(txt_numero.value) - 1
        page.update()
    
    def aumentar_clicked(event):
        txt_numero.value = int(txt_numero.value) + 1
        page.update()
    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=reducir_clicked),
                txt_numero,
                IconButton(icons.ADD, on_click=aumentar_clicked)
            ]
        )
    )


# Modo escritorio:
flet.app(target=main)
