import flet
from flet import (
    colors,
    icons,
    margin,
    AppBar,
    Container,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text
)


class TrelloApp:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.appbar_items = [
            PopupMenuItem(text='Login'),
            PopupMenuItem(),
            PopupMenuItem(text='Settings'),
        ]


if __name__ == '__main__':

    def main(page: Page):
        page.title = 'Flet Trello Clone - Trolli'
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200

        # app = TrelloApp()
        # page.add(app)

        page.update()


    flet.app(target=main, view=flet.WEB_BROWSER)
