import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = 'Ejemplo de Rutas'

    print('Ruta inicial:', page.route)

    def route_change(event):
        print('Ruta cambiada:', event.route)
        page.views.clear()

        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Flet app')),
                    ElevatedButton('Go to configuration', on_click=open_settings)
                ]
            )
        )

        if page.route == '/settings' or page.route == '/settings/mail':
            page.views.append(
                View(
                    '/settings',
                    [
                        AppBar(title=Text('Settings', bgcolor=colors.SURFACE_VARIANT)),
                        Text('Configuración', style='bodyMedium'),
                        ElevatedButton(
                            'Go to mail settings',
                            on_click=open_mail_settings
                        )
                    ]
                )
            )
        
        if page.route == '/settings/mail':
            page.views.append(
                View(
                    '/settings/mail',
                    [
                        AppBar(title=Text('Flet app'), bgcolor=colors.SURFACE_VARIANT),
                        Text('Mail settings')
                    ]
                )
            )
        
        page.update()

    def view_pop(event):
        print('View pop:', event.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_settings(event):
        page.go('/settings')
    
    def open_mail_settings(event):
        page.go('/settings/mail')
    
    page.go(page.route)


# Modo Web:
flet.app(target=main, view=flet.WEB_BROWSER)
