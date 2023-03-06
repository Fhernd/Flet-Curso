import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button Demo'

    btn_simple = ElevatedButton(text='Elevated Button')
    btn_simple_desactivado = ElevatedButton(text='Elevated Button desactivado', disabled=True)

    page.add(btn_simple)
    page.add(btn_simple_desactivado)


if __name__ == '__main__':
    flt.app(target=main)
