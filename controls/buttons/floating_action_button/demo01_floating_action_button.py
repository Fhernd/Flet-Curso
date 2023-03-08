import flet as flt
from flet import *


def main(page: Page):
    page.title = "Floating Action Button - Ejemplo"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = 'center'
    page.auto_scroll = True
    page.scroll = ScrollMode.HIDDEN

    app_bar = AppBar(
        title=Text('Floating Action Button', weight=FontWeight.BOLD, color=colors.BLACK87),
        bgcolor=colors.BLUE,
        center_title=True,
        actions=[
            IconButton(
                flt.icons.MENU,
                tooltip='Menu',
                icon_color=colors.BLACK87
            )
        ],
        color=colors.WHITE
    )

    page.appbar = app_bar

    page.count = 0

    def fab_pressed(event):
        page.add(ListTile(title=Text(f'Item {page.count}')))
        page.show_snack_bar(
            SnackBar(Text("Tile was added successfully!"), open=True) 
        )

        page.count += 1
    
    fab = FloatingActionButton(
        icon=flt.icons.ADD,
        tooltip='Add Tile',
        on_click=fab_pressed,
        bgcolor=colors.LIME_300
    )

    page.floating_action_button = fab

    page.add(Text('Press the FAB to add a tile!'))


if __name__ == '__main__':
    flt.app(target=main)
