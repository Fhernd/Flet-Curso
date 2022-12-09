import flet
from flet import Container, ElevatedButton, Page
from flet.animation import Animation


def main(page: Page):
    page.title = 'Container Demo - Animación'

    container = Container(
        width=200,
        height=200,
        bgcolor='red',
        animate=Animation(2000, 'bounceOut')
    )

    def animar_contenedor(event):
        container.width = 100 if container.width == 200 else 200
        container.height = 100 if container.height == 200 else 200

        container.bgcolor = 'blue' if container.bgcolor == 'red' else 'red'

        container.update()
    
    page.add(
        container,
        ElevatedButton('Animar Contenedor', on_click=animar_contenedor)
    )


if __name__ == '__main__':
    flet.app(target=main)
