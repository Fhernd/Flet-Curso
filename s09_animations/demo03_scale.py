import flet as ft
from flet.animation import Animation
from flet.transform import Scale


def main(page: ft.Page):
    contenedor = ft.Container(
        width=300,
        height=300,
        bgcolor='blue',
        border_radius=5,
        scale=Scale(scale=1),
        animate_scale=Animation(600, 'bounceIn')
    )

    def animate(event):
        contenedor.scale = 3
        page.update()
    
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 30

    page.add(
        contenedor,
        ft.ElevatedButton('Animar', on_click=animate)
    )


ft.app(target=main, view=ft.WEB_BROWSER)
