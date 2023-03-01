import flet as flt
from flet import *


def main(page: Page):
    rail = NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(
            icon=icons.CREATE,
            text='Agregar',
        ),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icons=icons.FAVORITE_BORDER,
                selected_icon=icons.FAVORITE,
                label='First'
            ),
            NavigationRailDestination(
                icons=icons.BOOKMARK_BORDER,
                selected_icon=Icon(icons.BOOKMARK),
                label='Second'
            ),
            NavigationRailDestination(
                icons=icons.SETTINGS_OUTLINED,
                selected_icon=Icon(icons.BOOKMARK),
                label='Settings'
            )
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index)
    )
