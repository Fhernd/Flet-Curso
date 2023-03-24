import flet as flt
from flet import *


def main(page: Page):
    page.title = "Shader Mask - Fade Out"

    page.add(
        Row([
            ShaderMask(
                Image(src="https://picsum.photos/100/200?2"),
                blend_mode=BlendMode.DST_IN,
                shader=LinearGradient(
                    begin=alignment.top_center,
                    end=alignment.bottom_center,
                    colors=[colors.BLACK, colors.TRANSPARENT],
                    stops=[0.5, 1.0]
                ),
                border_radius=10
            )
        ])
    )


if __name__ == "__main__":
    flt.app(target=main)

