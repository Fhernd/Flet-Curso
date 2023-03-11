import flet as ft


def main(page: ft.Page):
    page.title = "Text buttons with icons"
    page.add(
        ft.TextButton("Button with icon", icon="chair_outlined"),
        ft.TextButton(
            "Button with colorful icon",
            icon="park_rounded",
            icon_color="green400",
        ),
    )

ft.app(target=main)
