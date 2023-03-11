import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Text Button'

    tbn_primero = TextButton(text='Text Button')
    tbn_segundo = TextButton('Disabled button', disabled=True)

    page.add(
        tbn_primero,
        tbn_segundo
    )


if __name__ == '__main__':
    flt.app(target=main)
