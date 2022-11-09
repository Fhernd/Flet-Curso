import flet
from flet import Page, Row, Text


def main(page: Page):
    row_datos = Row(controls=[Text('Python'), Text('Flet'), Text('Flutter')])

    page.add(row_datos)


# Ejecución en el escritorio:
flet.app(target=main)
