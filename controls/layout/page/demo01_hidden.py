from time import sleep
import flet
from flet import Page, Text


def main(page: Page):
    page.add(Text('¡Holaaa!'))

    sleep(3)

    page.window_visible = True
    page.update()


if __name__ == '__main__':
    flet.app(target=main, view=flet.FLET_APP_HIDDEN)
