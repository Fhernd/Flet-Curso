import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Slider"

    page.add(
        Text('Slider por defecto:'),
        Slider(),
        Text('Slider deshabilitado:'),
        Slider(disabled=True),
    )


if __name__ == '__main__':
    flt.app(target=main)
