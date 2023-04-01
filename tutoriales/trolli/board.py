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
        