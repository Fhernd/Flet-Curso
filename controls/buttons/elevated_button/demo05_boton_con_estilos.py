import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button con Estilos Demo'

    btn_estilos = ElevatedButton(
        'Styled button 1',
        style=ButtonStyle(
            color={
                MaterialState.HOVERED: colors.WHITE,
                MaterialState.FOCUSED: colors.BLUE,
                MaterialState.DEFAULT: colors.BLACK,
            },
            bgcolor={
                MaterialState.FOCUSED: colors.PINK_200,
                "": colors.YELLOW,
            },
            padding={
                MaterialState.HOVERED: 20,
            },
            overlay_color=colors.TRANSPARENT,
            elevation={
                'pressed': 0,
                '': 1
            },
            animation_duration=500,
            side = {
                MaterialState.DEFAULT: BorderSide(1, colors.BLUE),
                MaterialState.HOVERED: BorderSide(1, colors.BLUE),
            },
            shape={
                MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                MaterialState.DEFAULT: RoundedRectangleBorder(radius=2),
            }
        )
    )

    page.add(btn_estilos)


if __name__ == '__main__':
    flt.app(target=main)
