import flet as flt
from flet import *


def main(page: Page):
    page.title = "Outlined Button - Demostración"

    obn_primero = OutlinedButton(text='Outlined Button')
    obn_segundo = OutlinedButton('Disabled button', disabled=True)

    page.add(obn_primero, obn_segundo)


if __name__ == '__main__':
    flt.app(target=main)
