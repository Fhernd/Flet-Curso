import flet as flt
from flet import *


def main(page: Page):
    page.title = "Window Drag Area"

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.add(
        Row([
            WindowDragArea(
                Container(Text('Drag this area to move, maximize and restore application window.'), bgcolor=colors.AMBER_300, padding=10, expand=True)
            ),
            IconButton(icons.CLOSE, on_click=lambda _: page.window_close())
        ])
    )


if __name__ == '__main__':
    flt.app(target=main)
