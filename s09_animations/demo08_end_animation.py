import flet as ft


def animation_end(event):
    print(dir(event))


def main(page: ft.Page):
    contenedor = ft.Container(
        width=200,
        height=200,
        bgcolor='blue',
        border_radius=10,
        animate_opacity=300,
        on_animation_end=animation_end
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
