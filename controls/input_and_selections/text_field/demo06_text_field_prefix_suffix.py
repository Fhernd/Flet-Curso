import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Text Field prefix and suffix"

    page.add(
        TextField(label="With prefix", prefix_text="https://"),
        TextField(label="With suffix", suffix_text=".com"),
        TextField(label="With prefix and suffix", prefix_text="https://", suffix_text=".com"),
        TextField(
            label="My favorite color",
            icon=icons.FORMAT_SIZE,
            hint_text="Type your favorite color",
            helper_text="You can type only one color",
            counter_text="0 symbols typed",
            prefix_icon=icons.COLOR_LENS,
            suffix_text="...is your color",
        )
    )


if __name__ == '__main__':
    flt.app(target=main)
