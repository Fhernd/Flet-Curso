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


if __name__ == '__main__':

    def main(page: Page):
        page.title = 'Flet Trello Clone - Trolli'
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200

        # app = TrelloApp()
        # page.add(app)

        page.update()


    flet.app(target=main, view=flet.WEB_BROWSER)
