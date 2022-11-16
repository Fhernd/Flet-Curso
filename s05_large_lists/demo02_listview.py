import flet
from flet import ListView, Page, Text


def main(page: Page):
    lvw_textos = ListView(expand=True, spacing=10)

    for i in range(5000):
        lvw_textos.controls.append(Text(f'Line {i}'))
    
    page.add(lvw_textos)


# Ejecutar en modo escritorio:
# flet.app(target=main)

# Ejecución en modo Web:
flet.app(target=main, view=flet.WEB_BROWSER)
