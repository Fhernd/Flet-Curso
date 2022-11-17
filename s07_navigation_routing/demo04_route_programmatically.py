import flet
from flet import ElevatedButton, Page, Text


def main(page: Page):
    page.add(Text(f'Ruta inicial: {page.route}'))

    def route_change(route):
        page.add(Text(f'Nueva ruta: {route.route}'))
    
    def go_store(event):
        page.route = '/tienda'
        page.update()
    
    page.on_route_change = route_change
    page.add(
        ElevatedButton('Ir a la tienda', on_click=go_store)
    )


flet.app(target=main, view=flet.WEB_BROWSER)
