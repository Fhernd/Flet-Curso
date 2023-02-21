import flet as ft
from flet import Image, ImageFit, Page, Row, Stack, Text


def main(page: Page):
    stack = Stack(
        [
            Image(
                src="https://picsum.photos/300/300",
                width=300,
                height=300,
                fit=ImageFit.CONTAIN,
            ),
            Row(
                [
                    Text(
                        'Paisaje',
                        color='white',
                        size=40,
                        weight='bold',
                        opacity=0.5,
                    )
                ],
                alignment='center',
            )
        ],
        width=300,
        height=300,
    )

    page.add(stack)


if __name__ == '__main__':
    ft.app(target=main)
