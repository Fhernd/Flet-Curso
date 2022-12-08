import flet
from flet import Container, Page, Row, Text, colors


def main(page: Page):
    page.title = "Container Demo - Contenedores"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    page.add(
        Row([
            Container(
                content=Text('No cliqueable'),
                margin=10,
                padding=10,
                alignment=flet.alignment.center,
                bgcolor=colors.AMBER,
                width=150,
                height=150,
                border_radius=10
            ),
            Container(
                content=Text('Cliqueable sin Ink'),
                margin=10,
                padding=10,
                alignment=flet.alignment.center,
                bgcolor=colors.GREEN_200,
                width=150,
                height=150,
                border_radius=10,
                on_click=lambda e: print('Clickeado sin Ink')
            ),
            Container(
                content=Text('Cliqueable con Ink'),
                margin=10,
                padding=10,
                alignment=flet.alignment.center,
                bgcolor=colors.CYAN_200,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print('Clickeado con Ink')
            ),
            Container(
                content=Text('Cliqueable transparente con Ink'),
                margin=10,
                padding=10,
                alignment=flet.alignment.center,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print('Clickeado transparente con Ink')
            ),
        ],
        alignment='center')
    )


if __name__ == '__main__':
    flet.app(target=main)
