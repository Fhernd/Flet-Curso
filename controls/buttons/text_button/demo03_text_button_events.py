import flet as ft
from flet import *


def main(page: Page):
    page.title = 'Text Button Events'

    def on_click(event):
        tbn.data += 1
        lbl_conteo.value = f'Conteo: {tbn.data}'
        page.update()
    
    tbn = TextButton('Click me', on_click=on_click, data=0)
    lbl_conteo = Text('Conteo: 0')

    page.add(tbn, lbl_conteo)


if __name__ == '__main__':
    ft.app(target=main)
