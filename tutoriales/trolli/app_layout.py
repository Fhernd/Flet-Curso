from flet import (
    border,
    border_radius,
    colors,
    icons,
    padding,
    ButtonStyle,
    Column,
    Container,
    Control,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    Text,
    TextButton,
    TextField
)

from sidebar import Sidebar
from data_store import DataStore


class AppLayout(Row):
    def __init__(self, app, page, store: DataStore, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app
        self.page = page

        self.on_resize = self.page_resize
        self.store: DataStore = store

        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            icon_color=colors.BLUE_GREY_400,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail
        )

        self.sidebar = Sidebar(self, self.store, page)

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

        self._active_view: Control = self.all_boards_view

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
        self.controls[-1] = self._active_view
        self.sidebar.sync_board_destinations()
        self.update()

    def set_board_view(self, i):
        """
        Establece la vista de un tablero como la vista activa.

        :param i: El índice del tablero a establecer como vista activa.
        """
        self.active_view = self.store.get_boards()[i]
        self.sidebar.bottom_nav_rail.selected_index = i
        self.sidebar.top_nav_rail.selected_index = None
        
        self.sidebar.update()
        self.page.update()
        self.page_resize()
    
    def set_all_boards_view(self):
        """
        Establece la vista de todos los tableros como la vista activa.
        """
        self.active_view = self.all_boards_view
        self.hydrate_all_boards_view()
        self.sidebar.top_nav_rail.selected_index = 0
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()
    
    def set_members_view(self):
        """
        Establece la vista de miembros como la vista activa.
        """
        self.active_view = self.members_view
        self.sidebar.top_nav_rail.selected_index = 1
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()
    
    def toggle_nav_rail(self, event):
        """
        Este método es llamado cuando se hace click en el botón de toggle de la barra lateral.

        :param event: El evento que disparó el click.
        """
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page_resize()
        self.page.update()

    def hydrate_all_boards_view(self):
        """
        Rehidrata la vista de todos los tableros.
        """
        self.all_boards_view.controls[-1] = Row([
            Container(
                content=Row([
                    Container(
                        content=Text(value=b.name),
                        data=b,
                        expand=True,
                        on_click=self.board_click
                    ),
                    Container(
                        content=PopupMenuButton(
                            items=[
                                PopupMenuItem(
                                    content=Text(
                                        value='Delete',
                                        style='labelMedium',
                                        text_align='center'
                                    ),
                                    on_click=self.delete_board,
                                    data=b
                                ),
                                PopupMenuItem(),
                                PopupMenuItem(
                                    content=Text(
                                        value='Archive',
                                        style='labelMedium',
                                        text_align='center'
                                    ),
                                ),
                            ]
                        ),
                        padding=padding.only(right=-10),
                        border_radius=border_radius.all(3)
                    ),
                ],
                alignment='spaceBetween',
                ),
                border=border.all(1, colors.BLACK38),
                border_radius=border_radius.all(5),
                bgcolor=colors.WHITE60,
                padding=padding.all(10),
                width=250,
                data=b
            )
            for b in self.app.boards
        ],
        wrap=True
        )

        self.sidebar.sync_board_destinations()
    
    def board_click(self, event):
        """
        Este método es llamado cuando se hace click en un tablero.

        :param event: El evento que disparó el click.
        """
        self.sidebar.bottom_nav_change(self.store.get_boards().index(event.control.dadta))
    
    def page_resize(self, event=None):
        """
        This method is called when the page is resized.

        :param event: The event that triggered the resize.
        :type event: flet.events.ResizeEvent
        """
        if type(self.active_view) is Board:
            self.active_view.resize(
                self.sidebar.visible, self.page.width, self.page.height
            )
        
        self.page.update()
    