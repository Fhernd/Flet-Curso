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
            self.inner_list.border = border.all(2, colors.BLACK38)
        
        self.update()
    
    