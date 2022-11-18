import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = 'Ejemplo de Rutas'

    def route_change(route):
        page.views.clear()

        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('App Flet'), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton('Visitar la tienda', on_click=lambda _: page.go('/tienda'))
                ]
            )
        )

        if page.route == '/tienda':
            page.views.append(
                View(
                    '/tienda',
                    [
                        AppBar(title=Text('Tienda'), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton('Inicio', on_click=lambda _: page.go('/'))
                    ]
                )
            )
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main)
