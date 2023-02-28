import flet as flt

from flet import *


def main(page: Page):
    page.title = "Card - Ejemplo"

    card = Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        leading=Icon(icons.ALBUM),
                        title=Text('The Enchanted Nightingale'),
                        subtitle=Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    Row(
                        [TextButton('Buy tickets'), TextButton('Listen')],
                        alignment='end',
                    )
                ]
            ),
            width=400,
            padding=10,
        )
    )

    page.add(card)


if __name__ == '__main__':
    flt.app(target=main)
