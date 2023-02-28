import flet as flt
from flet import *


def main(page: Page):
    row_contenido = Row([
        Container(
            bgcolor=colors.ORANGE_300,
            alignment=alignment.center,
            expand=True,
        ),
        VerticalDivider(),
        Container(
            bgcolor=colors.BROWN_300,
            alignment=alignment.center,
            expand=True,
        ),
        VerticalDivider(width=1, color='white'),
        Container(
            bgcolor=colors.BLUE_300,
            alignment=alignment.center,
            expand=True,
        ),
        VerticalDivider(width=9, thickness=3),
        Container(
            bgcolor=colors.GREEN_300,
            alignment=alignment.center,
            expand=True,
        ),
    ],
    spacing=0,
    expand=True
    )

    page.add(row_contenido)


if __name__ == '__main__':
    flt.app(target=main)
