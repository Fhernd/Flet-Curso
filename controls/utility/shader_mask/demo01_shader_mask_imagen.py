import flet as flt
from flet import *


def main(page: Page):
    page.title = "Shader Mask"

    page.add(
        Row([
            ShaderMask(
                Image(
                    src="https://picsum.photos/200/200?1",
                    width=200,
                    height=200,
                    fit=ImageFit.FILL
                ),
                blend_mode=BlendMode.MULTIPLY,
                shader=RadialGradient(
                    center=alignment.center,
                    radius=2.0,
                    colors=[colors.WHITE, colors.RED],
                    tile_mode=GradientTileMode.CLAMP
                )
            )
        ])
    )


if __name__ == "__main__":
    flt.app(target=main)
