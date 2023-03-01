import flet as flt
from flet import *


def main(page: Page):
    def check_item_clicked(event):
        event.control.checked = not event.control.checked
        page.update()
    
    page.appbar = AppBar(
        leading=Icon(icons.PALETTE),
        leading_width=40,
        title=Text('AppBar - Ejemplo'),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED),
            IconButton(icons.FILTER_3),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text='Item 1'),
                    PopupMenuItem(),
                    PopupMenuItem(
                        text='Checked item', checked=False, on_click=check_item_clicked
                    ),
                ]
            )
        ]
    )

    page.add(Text('Contenido de la página'))


if __name__ == '__main__':
    flt.app(target=main, view=flt.WEB_BROWSER)
