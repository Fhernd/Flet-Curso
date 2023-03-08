import flet as flt
from flet import *


def main(page: Page):
    page.title = "Filled Button"

    btn_primero = FilledButton(
        text="Primero",
    )

    btn_segundo = FilledButton(
        text="Segundo",
        disabled=True,
    )

    btn_tercero = FilledButton(
        text="Tercero",
        icon='add'
    )

    page.add(btn_primero)
    page.add(btn_segundo)
    page.add(btn_tercero)


if __name__ == '__main__':
    flt.app(target=main)
