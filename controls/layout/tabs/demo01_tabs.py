import flet as flt
from flet import *


def main(page: Page):
    tab_1 = Tab(
        text='Tab 1',
        content=Container(
            content=Text('Tab 1 content'),
            alignment='center'
        )
    )
    
    tab_2 = Tab(
        tab_content=Icon(icons.SEARCH),
        content=Text('This is Tab 2')
    )
    
    tab_3 = Tab(
        text='Tab 3',
        icon=icons.SETTINGS,
        content=Text('This is Tab 3')
    )

    tabs = Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[tab_1, tab_2, tab_3],
        expand=True
    )

    page.add(tabs)


if __name__ == '__main__':
    flt.app(target=main)
