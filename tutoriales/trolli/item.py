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

    def build(self):
        
        self.view = Draggable(
            content=DragTarget(
                group='items',
                content=self.card_item,
                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
            ),
            data=self
        )

        return self.view
    