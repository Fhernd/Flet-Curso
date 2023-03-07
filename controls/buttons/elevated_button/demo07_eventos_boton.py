import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button con Evento Click Demo'

    def on_hover(event):
        event.control.bgcolor = 'orange' if event.data == 'true' else 'yellow'
        event.control.update()
    
    btn_boton = ElevatedButton(
        "I'm changing my color on hover",
        bgcolor='yellow',
        on_hover=on_hover
    )

    page.add(btn_boton)


if __name__ == '__main__':
    flt.app(target=main)
