import flet
from flet import Page, Text


def main(page: Page):
    page.add(
        Text(value='¡Hola!')
    )


flet.app(target=main)
