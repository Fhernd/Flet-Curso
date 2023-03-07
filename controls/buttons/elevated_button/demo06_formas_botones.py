import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button con Formas Demo'

    page.padding = 30
    page.spacing = 30

    btn_primero = ElevatedButton(
        'Stadium',
        style=ButtonStyle(
            shape=StadiumBorder()
        )
    )

    btn_segundo = ElevatedButton(
        'Rounded rectangle',
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=10)
        )
    )

    btn_tercero = ElevatedButton(
        'Continuous rectangle',
        style=ButtonStyle(
            shape=CountinuosRectangleBorder(radius=30)
        )
    )

    btn_cuarto = ElevatedButton(
        'Beveled rectangle',
        style=ButtonStyle(
            shape=BeveledRectangleBorder(radius=10)
        )
    )

    btn_quinto = ElevatedButton(
        'Circle',
        style=ButtonStyle(
            shape=CircleBorder(),
            padding=30
        )
    )

    page.add(btn_primero)
    page.add(btn_segundo)
    page.add(btn_tercero)
    page.add(btn_cuarto)
    page.add(btn_quinto)


if __name__ == '__main__':
    flt.app(target=main)
