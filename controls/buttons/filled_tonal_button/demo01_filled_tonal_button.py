import flet as flt
from flet import *


def main(page: Page):
    page.title = "Filled Tonal Button - Ejemplo"

    btn_primero = FilledTonalButton(
        text="Filled tonal button"
    )

    btn_segundo = FilledTonalButton(
        'Disabled button', disabled=True
    )

    btn_tercero = FilledTonalButton(
        'Button with icon', icon='add'
    )

    page.add(btn_primero)
    page.add(btn_segundo)
    page.add(btn_tercero)


if __name__ == '__main__':
    flt.app(target=main)
