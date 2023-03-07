import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button Compuesto Demo'

    btn_iconos = ElevatedButton(
        width=150,
        content=Row([
            Icon(name=icons.FAVORITE, color='pink'),
            Icon(name=icons.AUDIOTRACK, color='green'),
            Icon(name=icons.BEACH_ACCESS, color='blue'),
        ],
        alignment='space_around')
    )

    btn_compuesto = ElevatedButton(
        content=Container(
            content=Column([
            Text(value='Compound button', size=20),
            Text(value='This is secondary text'),
            ],
            alignment='center',
            spacing=5),
            padding=padding.all(10)
        )
    )

    page.add(btn_iconos)
    page.add(btn_compuesto)


if __name__ == '__main__':
    flt.app(target=main)
