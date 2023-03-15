import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Text Field multiline"

    page.add(
        TextField(label='Standard', multiline=True),
        TextField(label='Disabled', disabled=True, value='line1\nline2\nline3\nline4\nline5', multiline=True),
        TextField(label='Auto adjusted height with max lines', multiline=True, min_lines=1, max_lines=3),
    )


if __name__ == '__main__':
    flt.app(target=main)
