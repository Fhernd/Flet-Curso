import flet as flt
from flet import *


def main(page: Page):
    page.title = "Outlined Button - Demostración"

    obn_primero = OutlinedButton(text='Button with icon', icon='chair_outlined')
    obn_segundo = OutlinedButton('Button with colorful icon', icon='park_rounded', icon_color='green40')

    page.add(obn_primero, obn_segundo)


if __name__ == '__main__':
    flt.app(target=main)
