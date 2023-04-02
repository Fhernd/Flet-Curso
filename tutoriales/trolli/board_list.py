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
    Row,
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

    def build(self):
        self.new_item_field = TextField(
            label='new card name',
            height=50,
            bgcolor=colors.WHITE,
            on_submit=self.add_item_handler
        )

        self.end_indicator = Container(
            bgcolor=colors.BLACK26,
            border_radius=border_radius.all(30),
            height=3,
            width=200,
            opacity=0.0
        )

        self.edit_field = Row([
            TextField(
                value=self.title,
                width=150,
                height=40,
                content_padding=padding.only(left=10, bottom=10),
            ),
            TextButton(
                text='Save',
                on_click=self.save_title
            )
        ])

        self.header = Row(
            controls=[
                Text(
                    value=self.title,
                    style='titleMedium',
                    text_align='left',
                    overflow='clip',
                    expand=True,
                ),
                Container(
                    PopupMenuButton(
                        items=[
                            PopupMenuItem(
                                content=Text('Edit'),
                                style='labelMedium',
                                text_align='center',
                                color=self.color,
                                on_click=self.edit_title
                            ),
                            PopupMenuItem(),
                            PopupMenuItem(
                                content=Text('Delete'),
                                style='labelMedium',
                                text_align='center',
                                color=self.color,
                                on_click=self.delete_list
                            ),
                            PopupMenuItem(),
                            PopupMenuItem(
                                content=Text('Move List'),
                                style='labelMedium',
                                text_align='center',
                                color=self.color,
                            ),
                        ],
                    ),
                    padding=padding.only(right=-10),
                ),
            ],
            alignment='spaceBetween',
        )
        