import flet
from flet import Page, Text


def main(page: Page):
    page.add(Text(f'Ruta inicial: {page.route}'))


flet.app(target=main, view=flet.WEB_BROWSER)
