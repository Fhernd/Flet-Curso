import flet
from flet import Container, Draggable, DragTarget, Page, Row, Text, alignment, border, colors


def main(page: Page):
    page.title = 'Ejemplo de Drag&Drop'

    def drag_accept(event):
        source = page.get_control(event.src_id)
        source.content.content.value = '0'
        event.control.content.content.value = '1'
        page.update()
    
    def drag_will_accept(event):
        event.control.content.border = border.all(
            2, colors.BLACK45 if event.data == 'true' else colors.RED
        )
        event.control.update()
    
    def drag_leave(event):
        event.control.content.border = None
        event.control.update()

    page.add(
        Row(
            [
                Draggable(
                    group='number',
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text('1', size=20),
                        alignment=alignment.center
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_200,
                        border_radius=5
                    ),
                    content_feedback=Text('1')
                ),
                Container(width=100),
                DragTarget(
                    group='number',
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text('0', size=20),
                        alignment=alignment.center
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave
                )
            ]
        )
    )


# Modo escritorio:
# flet.app(target=main)

# Modo Web:
flet.app(target=main, view=flet.WEB_BROWSER)
