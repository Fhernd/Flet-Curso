import flet
from flet import Container, ElevatedButton, Page
from flet.animation import Animation


def main(page: Page):

    contenedor = Container(
        width=150,
        height=150,
        bgcolor='red',
        animate=Animation(2000, 'bounceOut')
    )

    def animate_container(event):
        contenedor.width = 100 if contenedor.width == 150 else 150
        contenedor.height = 100 if contenedor.height == 150 else 150
        contenedor.bgcolor = 'blue' if contenedor.bgcolor == 'red' else 'red'
        contenedor.update()

    page.add(
        contenedor,
        ElevatedButton(
            'Animate',
            on_click=animate_container
        )
    )


# Modo escritorio:
flet.app(target=main)
