import flet as flt
from flet import *


def main(page: Page):
    page.title = "Floating Action Button - Ejemplo"

    fab = FloatingActionButton(
        content=Row(
            [
                Icon(flt.icons.ADD),
                Text('Add'),
            ],
            alignment="center", spacing=5
        ),
        bgcolor=colors.AMBER_300,
        shape=RoundedRectangleBorder(radius=5),
        width=100,
        mini=True,
    )

    page.floating_action_button = fab

    page.add(Text('Just a text!'))


if __name__ == '__main__':
    flt.app(target=main)
