import flet as ft


def main(page: ft.Page):
    contenedor = ft.Container(
        width=200,
        height=200,
        bgcolor='blue',
        border_radius=10,
        animate_opacity=300
    )

    def animate_opacity(event):
        contenedor.opacity = 0 if contenedor.opacity == 1 else 1
        contenedor.update()

    page.add(
        contenedor,
        ft.ElevatedButton(
            'Animate opacity',
            on_click=animate_opacity
        )
    )


ft.app(target=main)
