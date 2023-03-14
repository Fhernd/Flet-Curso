import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Dropdown hint'

    dbx = Dropdown(
        label='Color',
        hint_text='Choose your favorite color',
        options=[
            flt.dropdown.Option('Red'),
            flt.dropdown.Option('Green'),
            flt.dropdown.Option('Blue'),
        ],
        autofocus=True
    )

    page.add(
        dbx
    )


if __name__ == '__main__':
    flt.app(target=main)
