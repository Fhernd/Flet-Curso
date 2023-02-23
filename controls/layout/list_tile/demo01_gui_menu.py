import flet as flt
from flet import icons, Card, Column, Container, Icon, Image, ListTile, Page, PopupMenuButton, PopupMenuItem, Text


def main(page: Page):
    page.title = 'ListTile - Ejemplos'

    card = Card(
        content=Container(
            width=500,
            content=Column([
                ListTile(title=Text('One-line List Tile')),
                ListTile(title=Text('One-line dense list tile'), dense=True),
                ListTile(
                    leading=Icon(icons.SETTINGS),
                    title=Text('One-line sleected list tile'),
                    selected=True
                ),
                ListTile(
                    leading=Image(src='https://styles.redditmedia.com/t5_7jr5wm/styles/communityIcon_juop9fv9z76a1.png', fit='contain'),
                    title=Text('One-line with leading control'),
                ),
                ListTile(
                    title=Text('One-line with trailing control'),
                    trailing=PopupMenuButton(
                        icon=icons.MORE_VERT,
                        items=[
                            PopupMenuItem(text='Item 1'),
                            PopupMenuItem(text='Item 2'),
                        ]
                    )
                ),
                ListTile(
                    leading=Icon(icons.ALBUM),
                    title=Text('One-line with leading and trailing controls'),
                    trailing=PopupMenuButton(
                        icon=icons.MORE_VERT,
                        items=[
                            PopupMenuItem(text='Item 1'),
                            PopupMenuItem(text='Item 2'),
                        ]
                    )
                ),
                ListTile(
                    leading=Icon(icons.SNOOZE),
                    title=Text('Two-line with leading and trailing controls'),
                    subtitle=Text('Here is a second title.'),
                    trailing=PopupMenuButton(
                        icon=icons.MORE_VERT,
                        items=[
                            PopupMenuItem(text='Item 1'),
                            PopupMenuItem(text='Item 2'),
                        ]
                    )
                )
            ],
            spacing=0
            ),
            padding=flt.padding.symmetric(vertical=10)
        )
    )

    page.add(card)


if __name__ == '__main__':
    flt.app(target=main)
