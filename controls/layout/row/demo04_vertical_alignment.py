import flet
from flet import Column, Container, Page, Row, Text, colors


def main(page: Page):
    page.title = 'Row Demo - Alineación vertical'

    def generar_items(n):
        items = []

        for i in range(1, n + 1):
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

    def set_alineacion_vertical(alineacion):
        return Column(
            [
                Text(alineacion, size=16),
                Container(
                    content=Row(generar_items(3), vertical_alignment=alineacion),
                    bgcolor=colors.AMBER_100,
                    height=150,
                )
            ]
        )
    
    page.add(
        set_alineacion_vertical('start'),
        set_alineacion_vertical('center'),
        set_alineacion_vertical('end'),
    )


if __name__ == '__main__':
    flet.app(target=main)
