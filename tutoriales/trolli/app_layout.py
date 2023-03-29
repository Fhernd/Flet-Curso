from flet import (
    colors,
    icons,
    padding,
    ButtonStyle,
    Column,
    Container,
    Control,
    IconButton,
    Page,
    RoundedRectangleBorder,
    Row,
    Text,
    TextButton,
    TextField
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
                Container(
                    TextButton(
                        'Add new board',
                        icon=icons.ADD,
                        on_click=self.app.add_board,
                        style=ButtonStyle(
                            bgcolor={
                                "": colors.BLUE_200,
                                "hovered": colors.BLUE_400
                            },
                            shape={
                                "": RoundedRectangleBorder(radius=3)
                            }
                        )
                    )
                )
            ],
            padding=padding.only(top=15, right=50)),
            Row([
                TextField(
                    hint_text='Search all boards',
                    autofocus=False,
                    content_padding=padding.only(left=10),
                    width=200,
                    height=40,
                    text_size=12,
                    border_color=colors.BLACK26,
                    focused_border_color=colors.BLUE_ACCENT,
                    suffix_icon=icons.SEARCH,
                ),
            ]),
            Row([
                Text('No boards to Display')
            ])
        ],
        expand=True,
        )

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
