import flet as flt
from flet import *


def main(page: Page):
    page.title = "Haptic Feedback"

    hf = HapticFeedback()

    page.overlay.append(hf)

    page.add(
        ElevatedButton("Heavy impact", on_click=lambda _: hf.heavy_impact()),
        ElevatedButton("Medium impact", on_click=lambda _: hf.medium_impact()),
        ElevatedButton("Light impact", on_click=lambda _: hf.light_impact()),
        ElevatedButton("Vibrate", on_click=lambda _: hf.vibrate()),
    )


if __name__ == "__main__":
    flt.app(target=main)
