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

    def drag_accept(self, event):
        """
        Called when the item is dropped on a list.
        """
        src = self.page.get_control(event.src_id)

        if src.content.content == event.control.content:
            self.card_item.elevation = 1
            self.list.set_indicator_opacity(self, 0.0)
            event.control.update()
            return

        if src.data.list == self.list:
            self.list.add_item(chosen_control=src.data, swap_control=self)
            self.card_item.elevation = 1
            event.control.update()
            return
    
        self.list.add_item(src.data.item_text, swap_control=self)
        src.data.list.remove_item(src.data)
        self.list.set_indicator_opacity(self, 0.0)
        self.card_item.elevation = 1
        event.control.update()
    
    def drag_will_accept(self, event):
        """
        Called when the item is dragged over a list.

        If the item is dragged over the same list, then the indicator is hidden.

        param event: The event object.
        """
        if event.data == 'true':
            self.list.set_indicator_opacity(self, 1.0)
        
        self.card_item.elevation = 20 if event.data == 'true' else 1

        event.control.update()
    
    def drag_leave(self, event):
        """
        Called when the item is dragged away from a list.

        param event: The event object.
        """
        self.list.set_indicator_opacity(self, 0.0)
        self.card_item.elevation = 1
        
        event.control.update()
