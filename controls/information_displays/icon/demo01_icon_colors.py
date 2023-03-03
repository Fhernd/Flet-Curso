import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Icon Colors - Example'

    row = Row([
        Icon(name=icons.FAVORITE, color=colors.PINK),
        Icon(name=icons.AUDIOTRACK, color=colors.GREEN, size=30),
        Icon(name=icons.BEACH_ACCESS, color=colors.BLUE, size=50),
        Icon(name="settings", color='#c1c1c1', tooltip='Settings', size=80),
    ])

    page.add(row)


if __name__ == '__main__':
    flt.app(target=main)
