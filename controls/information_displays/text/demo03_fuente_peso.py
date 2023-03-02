import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Fuente y Peso - Ejemplo'

    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    lbl_texto = Text(
        'This is rendered with Roboto Slab',
        size=30,
        font_family='RobotoSlab',
        weight=FontWeight.BOLD,
    )

    def weight_on_change(event):
        lbl_texto.weight = f"w{int(event.control.value)}"
        lbl_texto.update()
    
    page.add(lbl_texto)
    page.add(Slider(
        min=100,
        max=900,
        divisions=8,
        label='{value}',
        width=500,
        on_change=weight_on_change
    ))


if __name__ == '__main__':
    flt.app(target=main)
