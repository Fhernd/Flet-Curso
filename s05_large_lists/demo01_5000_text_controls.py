import flet
from flet import Page, Text


def main(page: Page):
    for i in range(5000):
        page.controls.append(Text(f'Line {i}'))

    page.scroll = 'always'
    page.update()


# Ejecución en modo escritorio:
flet.app(target=main)
