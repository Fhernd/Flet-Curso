import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Navigation Bar - Ejemplo'
    nbr_principal = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.EXPLORE, label='Explorar'),
            NavigationDestination(icon=icons.COMMUTE, label='Commute'),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label='Commute',
            ),
        ]
    )

    page.navigation_bar = nbr_principal

    page.add(Text('¡Contenidooo!'))


if __name__ == '__main__':
    flt.app(target=main)
