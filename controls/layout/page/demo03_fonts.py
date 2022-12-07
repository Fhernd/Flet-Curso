import flet
from flet import Page, Text, Theme


def main(page: Page):
    page.title = 'Fuentes'

    page.fonts = {
        'Kanit': 'https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf'
    }

    page.theme = Theme(font_family='Kanit')

    page.add(
        Text('¡Hola con Kanit!', font_family='Kanit', size=30),
        Text('¡Hola con Open Sans!', font_family='Open Sans'),
    )


if __name__ == '__main__':
    flet.app(target=main)
