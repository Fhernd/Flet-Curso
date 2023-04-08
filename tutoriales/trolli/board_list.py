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

from item import Item
from data_store import DataSource

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
        """
        Builds the board list.
        """
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

        self.inner_list = Container(
            content=Column([
                self.header,
                self.new_item_field,
                TextButton(
                    content=Row([
                        Icon(icons.ADD),
                        Text('add card', color=colors.BLACK38)
                    ],
                    right=True),
                    on_click=self.add_item_handler,
                ),
                self.items,
                self.end_indicator
            ],
            spacing=4,
            tight=True,
            data=self.title,
            ),
            width=250,
            border=border.all(2, color=colors.BLACK12),
            border_radius=border_radius.all(5),
            bgcolor= self.color if len(self.color) else colors.WHITE,
            padding=padding.only(
                bottom=10,
                left=10,
                right=10,
                top=5
            ),
        )

        self.view = DragTarget(
            group='items',
            content=Draggable(
                group='items',
                content=DragTarget(
                    group='lists',
                    content=self.inner_list,
                    data=self,
                    on_accept=self.item_drag_accept,
                    on_will_accept=self.item_will_drag_accept,
                    on_leave=self.item_drag_leave,
                )
            )
        )

        return self.view
    
    def item_drag_accept(self, event):
        """
        Handles the drag accept event of the list.

        :param event: The event.
        """
        src = self.page.get_control(event.src_id)
        self.add_item(src.data.item_text)
        src.data.list.remove_item(src.data)
        self.end_indicator.opacity = 0.0
        self.update()
    
    def item_will_drag_accept(self, event):
        """
        Handles the drag will accept event of the list.

        :param event: The event.
        """
        if event.data == 'true':
            self.end_indicator.opacity = 1.0
        
        self.update()
    
    def item_drag_leave(self, event):
        """
        Handles the drag leave event of the list.

        :param event: The event.
        """
        self.end_indicator.opacity = 0.0
        self.update()
    
    def list_drag_accept(self, event):
        """
        Handles the drag accept event of the list.

        :param event: The event.
        """
        src = self.page.get_control(event.src_id)
        lists = self.board.board_lists
        
        to_index = lists.index(event.control.data)
        from_index = lists.index(src.content.data)

        lists[to_index], lists[from_index] = lists[from_index], lists[to_index]

        self.inner_list.border = border.all(2, colors.BLACK12)
        self.update()

    def list_will_drag_accept(self, event):
        """
        Handles the drag will accept event of the list.

        :param event: The event.
        """
        if event.data == 'true':
            self.inner_list.border = border.all(2, colors.BLACK)
        
        self.update()
    
    def list_drag_leave(self, event):
        """
        Handles the drag leave event of the list.

        :param event: The event.
        """
        self.inner_list.border = border.all(2, colors.BLACK12)
        self.update()
    
    def delete_list(self, event):
        """
        Deletes the list.

        :param event: The event.
        """
        self.board.remove_list(self, event)
    
    def edit_title(self, event):
        """
        Edits the title of the list.

        :param event: The event.
        """
        self.header.controls[0] = self.edit_field
        self.header.controls[1].visible = False
        self.update()
    
    def save_title(self, event):
        """
        Saves the title of the list.

        :param event: The event.
        """
        self.title = self.edit_field.controls[0].value
        self.header.controls[0] = Text(
            value=self.title,
            style='titleMedium',
            text_align='left',
            overflow='clip',
            expand=True,
        )
        self.header.controls[1].visible = True
        self.update()
    
    def add_item_handler(self, event):
        """
        Handles the add item event.

        :param event: The event.
        """
        if self.new_item_field.value == '':
            return

        self.add_item()
    
    def add_item(self, item: str = None, chosen_control: Draggable = None, swap_control: Draggable = None):
        """
        Adds an item to the list.

        :param item: The item to add.
        """
        control_list = [x.controls[1] for x in self.items.controls]

        to_index = control_list.index(swap_control) if swap_control else None
        from_index = control_list.index(chosen_control) if chosen_control else None

        control_to_add = Column([
            Container(
                bgcolor=colors.BLACK26,
                border_radius=border_radius.all(30),
                height=3,
                alignment=alignment.centerRight,
                width=200,
                opacity=0.0,
            )
        ])

        if ((from_index is not None)) and (to_index is not None):
            self.items.controls.insert(to_index, self.items.controls.pop(from_index))
        elif to_index is not None:
            new_item = Item(self, self.store, item)
            control_to_add.controls.append(new_item)
            self.items.controls.insert(to_index, control_to_add)
        else:
            new_item = Item(self, self.store, item) if item else Item(self, self.store, self.new_item_field.value)
            self.store.add_item(self.board_list_id, new_item)
            self.new_item_field.value = ''
        
        self.view.update()
        self.page.update()
    
    def remove_item(self, item: Item):
        """
        Removes an item from the list.

        :param item: The item to remove.
        """
        control_list = [x.controls[1] for x in self.items.controls]

        del self.items.controls[control_list.index(item)]
        self.store.remove_item(self.board_list_id, item)

        self.view.update()
    
    def set_indicator_opacity(self, item, opacity: float):
        """
        Sets the opacity of the end indicator.

        :param opacity: The opacity to set.
        """
        control_list = [x.controls[1] for x in self.items.controls]
        self.items.controls[control_list.index(item)].controls[0].opacity = opacity

        self.view.update()
