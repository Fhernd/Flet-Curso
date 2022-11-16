import flet
from flet import ListView, Page, Text


def main(page: Page):
    lvw_textos = ListView(expand=1, spacing=10, item_extent=50)
    page.add(lvw_textos)

    for i in range(5100):
        lvw_textos.controls.append(Text(f'Line {i}'))

        if i % 500 == 0:
            page.update()

    page.update()


# En el navegador:
flet.app(target=main, view=flet.WEB_BROWSER)
