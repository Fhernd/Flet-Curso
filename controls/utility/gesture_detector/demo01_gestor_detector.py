import flet as flt
from flet import *


def main(page: Page):
    page.title = "Gesture Detector Demo"

    def on_pan_update_1(event: DragUpdateEvent):
        container.top = max(0, container.top + event.delta_y)
        container.left = max(0, container.left + event.delta_x)
        container.update()
    
    def on_pan_update_2(event: DragUpdateEvent):
        event.control.top = max(0, event.control.top + event.delta_y)
        event.control.left = max(0, event.control.left + event.delta_x)
        event.control.update()


    gd = GestureDetector(
        mouse_cursor=MouseCursor.MOVE,
        drag_interval=50,
        on_pan_update=on_pan_update_1
    )

    container = Container(gd, bgcolor=colors.AMBER, width=50, height=50, left=0, top=0)

    gd1 = GestureDetector(
        mouse_cursor=MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update_2,
        left=100,
        top=100,
        content=Container(bgcolor=colors.BLUE, width=50, height=50),
    )

    page.add(Stack([container, gd1], width=1000, height=500))


if __name__ == "__main__":
    flt.app(target=main)
