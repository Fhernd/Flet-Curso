from flet import (
    alignment,
    border_radius,
    colors,
    icons,
    margin,
    padding,
    Column,
    Container,
    NavigationRail,
    NavigationRailDestination,
    Row,
    Text,
    UserControl
)


class Sidebar(UserControl):

    def __init__(self, app_layout, page):
        super().__init__()

        self.app_layout = app_layout
        self.page = page

        self.top_nav_items = [
            NavigationRailDestination(
                label_content=Text('Boards'),
                label='boards',
                icon=icons.BOOK_OUTLINED,
                selected_icon=icons.BOOK_OUTLINED,
            ),
            NavigationRailDestination(
                label_content=Text('Members'),
                label='Members',
                icon=icons.PERSON,
                selected_icon=icons.PERSON,
            )
        ]

        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type='all',
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=colors.BLUE_GREY,
            extended=True,
            expand=True
        )
