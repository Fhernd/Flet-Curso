import flet as flt
from flet import *


def main(page: Page):
    page.title = "Galería con GridView"
    page.theme_mode = ThemeMode.DARK
    page.padding = 50
    page.update()

    gvw_galeria = GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(gvw_galeria)

    for i in range(1, 1001):
        gvw_galeria.controls.append(
            Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            )
        )
    
    page.update()


if __name__ == "__main__":
    flt.app(target=main, view=flt.WEB_BROWSER)
