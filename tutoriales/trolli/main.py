import flet
from flet import (
    colors,
    icons,
    margin,
    Theme,
    AppBar,
    Container,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    UserControl,
)

from app_layout import AppLayout


class TrelloApp(UserControl):
    def __init__(self, page: Page) -> None:
        super().__init__()

        self.page = page

        self.appbar_items = [
            PopupMenuItem(text='Login'),
            PopupMenuItem(),
            PopupMenuItem(text='Settings'),
        ]

        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text('Trulli', size=32, text_align='start'),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items,
                    ),
                    margin=margin.only(left=50, right=25),
                )
            ]
        )

        self.page.appbar = self.appbar
        self.page.update()
    
    def build(self):
        self.layout = AppLayout(self, self.page)

        return self.layout


if __name__ == '__main__':

    def main(page: Page):
        page.title = 'Flet Trello Clone - Trolli'
        
        page.padding = 0
        page.theme = Theme(
            font_family={
                'Pacifico': '/Pacifico-Regular.ttf'
            }
        )
        page.theme.page_transitions.windows = 'cupertino'
        page.bgcolor = colors.BLUE_GREY_200

        page.update()
        app = TrelloApp(page)


    flet.app(target=main, assets_dir='../assets', view=flet.WEB_BROWSER)
