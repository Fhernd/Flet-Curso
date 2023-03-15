import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Text Field password"

    page.add(
        TextField(label='Password with reveal button', password=True, can_reveal_password=True),
    )


if __name__ == '__main__':
    flt.app(target=main)
