import flet
from flet import Container, ElevatedButton, OutlinedButton, Page, colors


def main(page: Page):
    page.title = "Container Demo - Color de Fondo"

    container_1 = Container(
        content=ElevatedButton('Elavated button in container'),
        bgcolor=colors.YELLOW,
        padding=5
    )

    container_2 = Container(
        content=ElevatedButton('Elavated button with opacity in container', opacity=0.5),
        bgcolor=colors.YELLOW,
        padding=5
    )

    container_3 = Container(
        content=OutlinedButton('Outlined button in container'),
        bgcolor=colors.YELLOW,
        padding=5
    )

    page.add(container_1, container_2, container_3)


if __name__ == '__main__':
    flet.app(target=main)
