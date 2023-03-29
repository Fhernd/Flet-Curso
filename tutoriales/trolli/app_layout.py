from flet import (
    colors,
    icons,
    padding,
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

        self.members_view = Text('Members View')

        self.all_boards_view = Column([
            Row([
                Container(
                    Text(value='Your Boards', style='headlineMedium'),
                    expand=True,
                    padding=padding.only(top=15)
                ),
            ])
        ])

        self._active_view: Control = Column(
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

    @property
    def active_view(self):
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()
    
    def toggle_nav_rail(self, event):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page.update()
