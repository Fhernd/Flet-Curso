import flet
from flet import Page, Text


def main(page: Page):
    page.title = 'Calculator'
    page.add(Text('Hello World!'))


if __name__ == '__main__':
    flet.app(target=main)
