import flet as flt
from flet import *


def main(page: Page):
    page.title = "Transparent Pointer"

    page.add(
        Stack([
            GestureDetector(
                on_tap=lambda _: print("tap!"),
                multi_tap_touches=3,
                on_multi_tap=lambda e: print("multi tap:", e.correct_touches),
                on_multi_long_press=lambda _: print('Multi tap long press')
            ),
            TransparentPointer(
                Container(
                    ElevatedButton('Test button'),
                    padding=50
                )
            )
        ],
        expand=True,
        )
    )


if __name__ == "__main__":
    flt.app(target=main)
