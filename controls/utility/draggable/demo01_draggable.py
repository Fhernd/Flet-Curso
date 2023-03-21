import flet
from flet import (
    Column,
    Container,
    Draggable,
    DragTarget,
    DragTargetAcceptEvent,
    Page,
    Row,
    border,
    colors,
)


def main(page: Page):
    page.title = "Draggable"

    def drag_will_accept(event):
        event.control.content.border = border.all(
            2, colors.BLACK45 if event.data == "true" else colors.RED
        )
        event.control.update()
    
    def drag_accept(event):
        src = page.get_control(event.src_id)
        event.control.content.bgcolor = src.content.bgcolor
        event.control.content.border = None
        event.control.update()
    
    def drag_leave(event):
        event.control.content.border = None
        event.control.update()
    
    page.add(
        Row(
            [
                Column(
                    [
                        Draggable(
                            group="color",
                            content=Container(
                                width=50,
                                height=50,
                                bgcolor=colors.CYAN,
                                border_radius=5,
                            ),
                            content_feedback=Container(
                                width=20,
                                height=20,
                                bgcolor=colors.CYAN,
                                border_radius=3,
                            ),
                        ),
                        Draggable(
                            group="color",
                            content=Container(
                                width=50,
                                height=50,
                                bgcolor=colors.YELLOW,
                                border_radius=5,
                            ),
                        ),
                        Draggable(
                            group="color1",
                            content=Container(
                                width=50,
                                height=50,
                                bgcolor=colors.GREEN,
                                border_radius=5,
                            ),
                        ),
                    ]
                ),
                Container(width=100),
                DragTarget(
                    group="color",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_100,
                        border_radius=5,
                    ),
                    on_will_accept=drag_will_accept,
                    on_accept=drag_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )


if __name__ == "__main__":
    flet.app(target=main)
