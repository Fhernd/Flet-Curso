import flet
from flet import Page, Row, Text


def main(page: Page):
    lenguajes = ['Python', 'Flet', 'Flutter']
    etiquetas = []

    for e in lenguajes:
        etiquetas.append(Text(e))

    row_datos = Row(controls=etiquetas)

    page.add(row_datos)


# Ejecución en el escritorio:
flet.app(target=main)
