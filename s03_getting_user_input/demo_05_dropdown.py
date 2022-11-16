import flet
from flet import Dropdown, ElevatedButton, Page, Text, dropdown


def main(page: Page):
    def submit_clicked(event):
        lbl_resultado.value = f' El valor del dropdown es: {cbx_color.value}'
        page.update()


    lbl_resultado = Text()

    btn_submit = ElevatedButton(text='Submit', on_click=submit_clicked)

    cbx_color = Dropdown(
        width=100,
        options= [
            dropdown.Option('Rojo'),
            dropdown.Option('Verde'),
            dropdown.Option('Azul')
        ]
    )

    page.add(cbx_color, btn_submit, lbl_resultado)


flet.app(target=main)
