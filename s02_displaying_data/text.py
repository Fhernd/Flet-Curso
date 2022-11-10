import flet
from flet import Page, Text


def main(page: Page):
    lbl_texto = Text(
        value='¡Flet y Python!',
        size=30,
        color='green',
        bgcolor='black',
        weight='bold',
        italic=True
    )

    page.add(lbl_texto)


# Aplicación de escritorio:
flet.app(target=main)
