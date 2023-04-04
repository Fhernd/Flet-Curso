from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board_list import BoardList

import itertools

from flet import (
    border_radius,
    Card,
    Checkbox,
    Container,
    Draggable,
    DragTarget,
    Row,
    UserControl,
)

from data_store import DataStore


class Item(UserControl):
    id_counter = itertools.count()

    def __init__(self, list: 'BoardList', store: DataStore, item_text: str):
        super().__init__()

        self.item_id = next(Item.id_counter)
        self.store: DataStore = store
        self.list = list
        self.item_text = item_text

        self.card_item = Card(
            content=Row([
                Container(
                    content=Checkbox(
                        label=f'{self.item_text}',
                        width=200,
                    ),
                    border_radius=border_radius.all(5),
                ),
            ],
            width=200,
            wrap=True
            ),
            elevation=1,
            data=self.list
        )
