import flet as flt
from flet import *


def main(page: Page):
    page.title = "Icon Button - Demostración"

    def toggle_icon_button(event):
        event.control.selected = not event.control.selected
        event.control.update()
    

    ibn_bateria = IconButton(
        icon=icons.BATTERY_1_BAR,
        selected_icon=icons.BATTERY_FULL,
        on_click=toggle_icon_button,
        selected=False,
        style=ButtonStyle(color={'selected': colors.GREEN, '': colors.RED})
    )

    page.add(ibn_bateria)


if __name__ == '__main__':
    flt.app(target=main)
