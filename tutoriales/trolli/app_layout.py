from flet import (
    colors,
    icons,
    Column,
    Container,
    Control,
    IconButton,
    Page,
    Row,
    Text
)

from sidebar import Sidebar


class AppLayout(Row):
    def __init__(self, app, page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app
        self.page = page
        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            icon_color=colors.BLUE_GREY_400,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail
        )

        self.sidebar = Sidebar(self, page)

        self.active_view: Control = Column(
            controls=[
                Text('Active View')
            ],
            alignment='center',
            horizontal_alignment='center',
        )

        self.controls = [
            self.sidebar,
            self.toggle_nav_rail_button,
            self.active_view
        ]
