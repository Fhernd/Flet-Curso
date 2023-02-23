import flet as flt
from flet import icons, Card, Column, Container, Icon, Image, ListTile, Page, Text


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
                )
            ])
        )
    )
    