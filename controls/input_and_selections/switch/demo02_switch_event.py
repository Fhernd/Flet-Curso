import flet as flt
from flet import *


def main(page: Page):
    page.page_title = "Input and Selections - Switch event"

    def switch_changed(event):
        page.theme_mode = (
            ThemeMode.DARK if page.theme_mode == ThemeMode.LIGHT else ThemeMode.LIGHT
        )

        swt_tema.label = (
            'Tema oscuro' if page.theme_mode == ThemeMode.DARK else 'Tema claro'
        )

        page.update()
    

    page.theme_mode = ThemeMode.LIGHT

    swt_tema = Switch(
        label='Tema claro',
        on_change=switch_changed
    )

    page.add(swt_tema)


if __name__ == '__main__':
    flt.app(target=main)
