import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button con Íconos Demo'

    btn_silla = ElevatedButton(text='Elevated Button', icon='chair_outlined')
    btn_arbol = ElevatedButton(text='Elevated Button desactivado', icon='park_rounded', icon_color='green400')

    page.add(btn_silla)
    page.add(btn_arbol)


if __name__ == '__main__':
    flt.app(target=main)
