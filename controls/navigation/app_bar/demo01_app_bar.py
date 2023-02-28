import flet as flt
from flet import *


def main(page: Page):
    def check_item_clicked(event):
        event.control.checked = not event.control.checked
        page.update()    


if __name__ == '__main__':
    flt.app(target=main)
