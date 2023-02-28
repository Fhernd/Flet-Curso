import flet as flt

from flet import *


def main(page: Page):
    col_contenido = Column([
        Container(
            bgcolor=colors.AMBER,
            alignment=alignment.center,
            expand=True,
        ),
        Divider(),
        Container(
            bgcolor=colors.PINK,
            alignment=alignment.center,
            expand=True,
        ),
        Divider(
            height=1,
            color='white'
        ),
        Container(
            bgcolor=colors.BLUE_300,
            alignment=alignment.center,
            expand=True,
        ),
        Divider(height=1, thickness=3),
        Container(
            bgcolor=colors.DEEP_PURPLE_300,
            alignment=alignment.center,
            expand=True,
        )
        ],
        spacing=0,
        expand=True,
    )

    page.add(col_contenido)


if __name__ == '__main__':
    flt.app(target=main)
