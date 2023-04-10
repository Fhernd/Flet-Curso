import flet
from flet import (
    colors,
    icons,
    margin,
    padding,
    Theme,
    AppBar,
    Container,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    UserControl,
    View
)

from app_layout import AppLayout
from data_store import DataStore
from memory_store import InMemoryStore


class TrelloApp(UserControl):
    """
    The main app.
    """
    def __init__(self, page: Page, store: DataStore) -> None:
        """
        Create a new app.

        :param page: The page that contains the app.
        """
        super().__init__()

        self.page = page
        self.store: DataStore = store

        self.page.on_route_change = self.route_change

        self.boards = self.store.get_boards()

        self.login_profile_button = PopupMenuItem(text='Log in', on_click=self.login)

        self.appbar_items = [
            self.login_profile_button,
            PopupMenuItem(),
            PopupMenuItem(text='Settings'),
        ]

        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text('Trulli', font_family='Pacifico', size=32, text_align='start'),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items,
                    ),
                    margin=margin.only(left=50, right=25),
                ),
            ],
        )

        self.page.appbar = self.appbar
        self.page.update()
    
    def build(self):
        """
        Build the app.

        :return: The app layout.
        """
        self.layout = AppLayout(
            self,
            self.page,
            self.store,
            tight=True,
            expand=True,
            vertical_alignment='start'
        )

        return self.layout

    def initialize(self):
        """
        Initialize the app.
        """
        self.page.views.clear()
        self.page.views.append(
            View(
                '/',
                [self.appbar, self.layout],
                padding=padding.all(0),
                bgcolor=colors.BLUE_GREY_200,
            )
        )

        self.page.update()

        if len(self.boards) == 0:
            self.create_new_board('My first board')
        
        self.page.go('/')
    
    def login(self, event):
        """
        Log in to the app.

        :param event: The event that triggered this action.
        """
        pass
    
    def route_change(self, event):
        """
        Handle a route change.

        :param event: The event that triggered this action.
        """
        pass
    
    def add_board(self, board):
        """
        Add a board to the app.

        :param board: The board to add.
        """
        pass

    def create_new_board(self, name):
        """
        Create a new board.

        :param name: The name of the new board.
        """
        pass

    def delete_board(self, event):
        """
        Delete a board.

        :param event: The event that triggered this action.
        """
        pass


def main(page: Page):
    page.title = 'Flet Trello Clone - Trolli'
    
    page.padding = 0
    page.theme = Theme(font_family='Verdana')
    page.theme.page_transitions.windows = 'cupertino'
    page.bgcolor = colors.BLUE_GREY_200

    app = TrelloApp(page, InMemoryStore)
    page.add(app)
    page.update()

    app.initialize()


if __name__ == '__main__':
    flet.app(target=main, assets_dir='../assets', view=flet.WEB_BROWSER)
