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
    
    def create_list(self, event):
        """
        Creates a new list for this board.
        """
        option_dict = {
            colors.LIGHT_GREEN: self.color_option_creator(colors.LIGHT_GREEN),
            colors.RED_200: self.color_option_creator(colors.RED_200),
            colors.AMBER_500: self.color_option_creator(colors.AMBER_500),
            colors.PINK_300: self.color_option_creator(colors.PINK_300),
            colors.ORANGE_300: self.color_option_creator(colors.ORANGE_300),
            colors.LIGHT_BLUE: self.color_option_creator(colors.LIGHT_BLUE),
            colors.DEEP_ORANGE_300: self.color_option_creator(colors.DEEP_ORANGE_300),
            colors.PURPLE_100: self.color_option_creator(colors.PURPLE_100),
            colors.RED_700: self.color_option_creator(colors.RED_700),
            colors.TEAL_500: self.color_option_creator(colors.TEAL_500),
            colors.YELLOW_400: self.color_option_creator(colors.YELLOW_400),
            colors.PURPLE_400: self.color_option_creator(colors.PURPLE_400),
            colors.BROWN_300: self.color_option_creator(colors.BROWN_300),
            colors.CYAN_500: self.color_option_creator(colors.CYAN_500),
            colors.BLUE_GREY_500: self.color_option_creator(colors.BLUE_GREY_500),
        }

        def set_color(event):
            color_options.data = event.control.data

            for k, v in option_dict.items():
                if k == event.control.data:
                    v.border = border.all(3, colors.BLACK26)
                else:
                    v.border = None
            
            dialog.content.update()
    