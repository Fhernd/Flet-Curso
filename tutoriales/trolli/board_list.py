from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board

import itertools
from flet import (
    alignment,
    border,
    border_radius,
    colors,
    icons,
    padding,
    Column,
    Container,
    Draggable,
    DragTarget,
    Icon,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    TextButton,
    TextField,
    UserControl
)

from tiem import Item
from data_source import DataSource

class BoardList(UserControl):
    id_counter = itertools.count()

    def __init__(self, board: 'Board', store: DataSource, title: str, color: str = ''):
        """
        Creates a new board list.

        :param board: The board that this list belongs to.
        :param store: The data store.
        :param title: The title of the list.
        :param color: The color of the list.
        """
        super().__init__()

        self.board_list_id = next(BoardList.id_counter)
        self.store: DataSource = store
        self.board: Board = board
        self.title = title
        self.color = color
        self.items = Column([], tight=True, spacing=4)
        self.items.controls = self.store.get_items(self.board_list_id)
