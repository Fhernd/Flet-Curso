import flet as flt
from flet import *


def main(page: Page):
    page.title = "Shake Detector"

    shd = ShakeDetector(
        minimum_shake_count=2,
        shake_slop_time_ms=300,
        shake_count_reset_time_ms=1000,
        on_shake=lambda _: print('Shake!')
    )

    page.overlay.append(shd)

    page.add(Text('Program body'))


if __name__ == "__main__":
    flt.app(target=main)
