import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Imagenes - Ejemplo'
    page.theme_mode = ThemeMode.LIGHT
    page.padding = 50
    page.update()

    imagen = Image(
        src='https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
        width=200,
        height=200,
        tooltip='Python Logo',
        fit=ImageFit.CONTAIN,
    )

    page.add(imagen)

    images = Row(expand=1, wrap=False, scroll='always')

    for i in range(31):
        images.controls.append(Image(
            src=f'https://picsum.photos/200/200?{i}',
            width=200,
            height=200,
            tooltip=f'Image {i}',
            fit=ImageFit.CONTAIN,
        ))
    
    page.add(images)


if __name__ == '__main__':
    flt.app(target=main)
