from math import pi
import flet as ft
from flet.animation import Animation
from flet.transform import Rotate


def main(page: ft.Page):
    contenedor = ft.Container(
        width=100,
        height=70,
        bgcolor='blue',
        border_radius=5,
        rotate=Rotate(0, alignment=ft.alignment.center),
        animate_rotation=Animation(duration=1200, curve='bounceOut')
    )

    def animate(event):
        contenedor.rotate.angle += pi / 2
        page.update()
    
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 30

    page.add(
        contenedor,
        ft.ElevatedButton('Animar', on_click=animate)
    )


ft.app(target=main)
