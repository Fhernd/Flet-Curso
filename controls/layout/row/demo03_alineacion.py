import flet
from flet import Column, Container, Page, Row, Text, colors


def main(page: Page):
    page.title = 'Row Demo - Alineación'

    def generar_items(contador):
        items = []

        for i in range(1, contador + 1):
            items.append(
                Container(
                    content=Text(f'{i}'),
                    alignment=flet.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=colors.AMBER_500
                )
            )
        
        return items
    
    def establecer_alineacion_fila(alineacion):
        return Column([
            Text(alineacion, size=16),
            Container(
                content=Row(generar_items(3), alignment=alineacion),
                bgcolor=colors.AMBER_100,
            )
        ])
    
    page.add(
        establecer_alineacion_fila('start'),
        establecer_alineacion_fila('center'),
        establecer_alineacion_fila('end'),
        establecer_alineacion_fila('spaceBetween'),
        establecer_alineacion_fila('spaceAround'),
        establecer_alineacion_fila('spaceEvenly')
    )


if __name__ == '__main__':
    flet.app(target=main)
