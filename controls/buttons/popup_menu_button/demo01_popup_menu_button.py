import flet as flt
from flet import *


def main(page: Page):
    def check_item_clicked(event):
        event.control.checked = not event.control.checked
        page.update()
    
    pop_principal = PopupMenuButton(
        items=[
            PopupMenuItem(text='Item 1'),
            PopupMenuItem(icon=icons.POWER_INPUT, text='Check power'),
            PopupMenuItem(
                content=Row([
                    Icon(icons.HOURGLASS_TOP_OUTLINED),
                    Text('Item with a custom content')
                ]),
                on_click=lambda _: print("Button with a custom content clicked!")
            ),
            PopupMenuItem(),
            PopupMenuItem(
                text='Checked item',
                checked=False,
                on_click=check_item_clicked
            )
        ]
    )

    page.add(pop_principal)


if __name__ == '__main__':
    flt.app(target=main)
