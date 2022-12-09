import flet
from flet import Column, Container, ContainerTapEvent, Page, Text, colors


def main(page: Page):
    page.title = 'Container Demo - Eventos'

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    lbl_texto = Text()

    def container_on_click(event: ContainerTapEvent):
        lbl_texto.value = f'local_x: {event.local_x}, local_y: {event.local_y}, global_x: {event.global_x}, global_y: {event.global_y}'
        lbl_texto.update()
    
    page.add(
        Column([
            Container(
                content=Text('Contener cliqueable'),
                alignment=flet.alignment.center,
                bgcolor=colors.GREEN_200,
                width=200,
                height=200,
                border_radius=10,
                on_click=container_on_click
            ),
            lbl_texto
        ])
    )


if __name__ == '__main__':
    flet.app(target=main)
