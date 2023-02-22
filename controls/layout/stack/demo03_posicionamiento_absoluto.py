import flet as flt
from flet import colors, Column, Container, Page, Stack


def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    stack = Stack([
        Container(width=20, height=20, bgcolor=colors.RED, border_radius=5),
        Container(width=20, height=20, bgcolor=colors.YELLOW, border_radius=5, right=0),
        Container(width=20, height=20, bgcolor=colors.BLUE, border_radius=5, right=0, bottom=0),
        Container(width=20, height=20, bgcolor=colors.GREEN, border_radius=5, left=0, bottom=0),
        Column(
            [
                Container(width=20, height=20, bgcolor=colors.PURPLE, border_radius=5),
            ],
            left=35,
            top=35,
        )
    ])

    container = Container(stack,
        border_radius=8,
        padding=5,
        width=100,
        height=100,
        bgcolor=colors.BLACK,
    )

    page.add(container)


if __name__ == '__main__':
    flt.app(target=main)
