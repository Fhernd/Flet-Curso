import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Slider event"

    def slider_changed(event):
        lbl_estado.value = f'El slider cambió: {event.control.value}'
        
        page.update()
    
    lbl_estado = Text()

    page.add(
        Text('Slider con evento de cambio:'),
        Slider(on_change=slider_changed, min=0, max=100, divisions=10, label='{value}%'),
    )
    page.add(lbl_estado)


if __name__ == '__main__':
    flt.app(target=main)
