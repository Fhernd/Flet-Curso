import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Slider"

    page.add(
        Text('Slider con  valor:'),
        Slider(value=0.3),
        Text('Slider con  valor, rango y etiqueta:'),
        Slider(min=0, max=100, divisions=10, label='{value}%'),
    )


if __name__ == '__main__':
    flt.app(target=main)
