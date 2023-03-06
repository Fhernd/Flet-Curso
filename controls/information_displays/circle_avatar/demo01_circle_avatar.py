import flet as flt
from flet import *


def main(page: Page):
    page.title = 'CircleAvatar - Ejemplo 1'

    cra_git_hub = CircleAvatar(
        foreground_image_url='https://avatars.githubusercontent.com/u/1562371?s=88&v=4',
        content=Text('JO')
    )

    cra_git_hub_fallback = CircleAvatar(
        foreground_image_url='https://avatars.githubusercontent.com/u/user/1562371?s=88&v=4',
        content=Text('JO')
    )

    cra_text = CircleAvatar(
        content=Icon(icons.ABC),
    )

    cra_color = CircleAvatar(
        content=Icon(icons.WARNING_ROUNDED),
        color=colors.YELLOW_200,
        bgcolor=colors.AMBER_700,
    )

    stk_contenido = Stack(
        [
            CircleAvatar(
                foreground_image_url="https://avatars.githubusercontent.com/u/1562371?s=88&v=4"
            ),
            Container(
                content=CircleAvatar(bgcolor=colors.GREEN, radius=5),
                alignment=alignment.bottom_left,
            ),
        ],
        width=40,
        height=40,
    )

    page.add(cra_git_hub)
    page.add(cra_git_hub_fallback)
    page.add(cra_text)
    page.add(cra_color)
    page.add(stk_contenido)


if __name__ == '__main__':
    flt.app(target=main)
