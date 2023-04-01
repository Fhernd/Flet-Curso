import itertools
from flet import (
    alignment,
    colors,
    border,
    border_radius,
    icons,
    margin,
    padding,
    AlertDialog,
    Column,
    Container,
    ElevatedButton,
    FloatingActionButton,
    Row,
    Text,
    TextField,
    UserControl
)

from board_list import BoardList
from data_store import DataStore


class Board(UserControl):
    id_counter = itertools.count()

    def __init__(self, app, store: DataStore, name: str):
        super().__init__()

        self.board_id = next(Board.id_counter)
        self.store: DataStore = store
        self.app = app
        self.name = name

        self.add_list_button = FloatingActionButton(
            icon=icons.ADD,
            text='add a list',
            height=30,
            on_click=self.create_list
        )

        self.board_lists = [
            self.add_list_button
        ]
        
        for l in self.store.get_lists_by_board(self.board_id):
            self.add_list(l)
        
        self.list_wrap = Row(
            self.board_lists,
            vertical_alignment='start',
            visible=True,
            scroll='auto',
            width=(self.app.page.width  - 310),
            height=(self.app.page.height - 95),
        )
    
    def build(self):
        """
        Build the view for this board.
        """
        self.view = Container(
            content=Column(
                controls=[
                    self.list
                ],
                scroll='auto',
                expand=True,
            ),
            data=self,
            margin=margin.all(0),
            padding=padding.only(top=10, right=0),
            height=self.app.page.height,
        )

        return self.view
        
    def resize(self, nav_rail_extended, width, height):
        """
        Resizes the board to fit the new width and height.
        """
        self.list_wrap.width = (width - 310) if nav_rail_extended else (width - 50)
        self.view.height = height
        self.list_wrap.update()
        self.view.update()
    