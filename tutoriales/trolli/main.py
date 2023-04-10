import flet
from flet import (
    colors,
    icons,
    margin,
    padding,
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    TextField,
    Theme,
    UserControl,
    View
)

from app_layout import AppLayout
from data_store import DataStore
from memory_store import InMemoryStore
from user import User


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
        def close_dialog(event):
            if user_name.value == '' or password.value == '':
                user_name.error_text = 'Please enter a user name.'
                password.error_text = 'Please enter a password.'
                
                self.page.update()
                
                return
            else:
                user = User(user_name.value, password.value)
                
                if user not in self.store.get_users():
                    self.store.add_user(user)
                
                self.user = user_name.value
                self.page.client_storage.set('current_user', user_name.value)
            
            dialog.open = False

            self.appbar_items[0] = PopupMenuItem(text=f"{self.page.client_storage.get('current_user')}'s Profile")

            self.page.update()
        
        user_name = TextField(label='User name')
        password = TextField(label='Password', password=True)

        dialog = AlertDialog(
            title=Text('Please enter your login credentials'),
            content=Column([
                user_name,
                password,
                ElevatedButton(text='Login', on_click=close_dialog)
            ],
            tight=True
            ),
            on_dismiss=lambda e: print('Modal dialog dismissed!')
        )

        self.page.dialog = dialog
        dialog.open = True

        self.page.update()
    
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
