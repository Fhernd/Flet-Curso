import flet
from flet import Container, ElevatedButton, Page
from flet.animation import Animation
from flet.transform import Offset


def main(page: Page):
    contenedor = Container(
        width=150,
        height=150,
        bgcolor='blue',
        border_radius=10,
        offset=Offset(-2, 0),
        animate_offset=Animation(100)
    )

    def animate(event):
        contenedor.offset = Offset(0, 0)
        contenedor.update()
    
    page.add(
        contenedor,
        ElevatedButton('Revelar', on_click=animate)
    )


flet.app(target=main)
