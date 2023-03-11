import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Text Button Compound'

    tbn_primero = TextButton(
        width=150,
        content=Row([
            Icon(name=icons.FAVORITE, color='pink'),
            Icon(name=icons.AUDIOTRACK, color='green'),
            Icon(name=icons.BEACH_ACCESS, color='blue'),
        ],
        alignment='space_around',
        )
    )

    tbn_segundo = TextButton(
        content=Container(
            content=Column([
                Text(value='Compound Button', size=20),
                Text(value='This is secondary text'),
            ],
            alignment='center',
            spacing=5
            ),
            padding=padding.all(10)
        )
    )

    page.add(tbn_primero, tbn_segundo)


if __name__ == '__main__':
    flt.app(target=main)
