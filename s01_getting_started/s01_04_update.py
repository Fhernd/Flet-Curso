import time

import flet
from flet import Page, Text


def main(page: Page):
    lbl_texto = Text()
    page.add(lbl_texto)

    for i in range(10):
        lbl_texto.value = f'Step: {i}'
        page.update()

        time.sleep(1)


# Ejecución en el escritorio:
# flet.app(target=main)

# Ejecución en el navegador Web:
flet.app(target=main, view=flet.WEB_BROWSER)
