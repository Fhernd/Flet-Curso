import flet as flt
from flet import *


def main(page: Page):
    page.title = "Icon Button - Demostración"

    ibn_primero = IconButton(
        icon=icons.PAUSE_CIRCLE_FILLED_ROUNDED,
        icon_color='blue400',
        icon_size=20,
        tooltip='Pause record'
    )

    ibn_segundo = IconButton(
        icon=icons.DELETE_FOREVER_ROUNDED,
        icon_color='pink600',
        icon_size=40,
        tooltip='Delete record'
    )

    row = Row([
        ibn_primero,
        ibn_segundo
    ])

    page.add(row)


if __name__ == '__main__':
    flt.app(target=main, view=flt.WEB)
