import flet
from flet import Page, Text


def main(page: Page):
    page.add(Text(f'Ruta incial: {page.route}'))

    def route_change(route):
        page.add(Text(f'Nueva ruta: {route.route}'))
    
    page.on_route_change = route_change
    page.update()


flet.app(target=main, view=flet.WEB_BROWSER)
