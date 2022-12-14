import flet
from flet import Column, Container, Page, Row, Slider, Text, alignment, border_radius, colors

def main(page: Page):
    def generar_items(n):
        items = []

        for i in range(1, n + 1):
            items.append(
                Container(
                    content=Text(f"{i}"),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_500,
                    width=50,
                    height=50,
                    border_radius=border_radius.all(5)
                )
            )
        
        return items
    
    def set_column_alignment(alineacion):
        return Column([
            Text(alineacion, size=10),
            Container(
                content=Column(generar_items(3), alignment=alineacion),
                bgcolor=colors.AMBER_100,
                height=400
            )
        ])
    
    page.add(
        Row(
            [
                set_column_alignment('start'),
                set_column_alignment('center'),
                set_column_alignment('end'),
                set_column_alignment('spaceBetween'),
                set_column_alignment('spaceAround'),
                set_column_alignment('spaceEvenly'),
            ],
            spacing=30,
            alignment='start'
            )
    )
    

if __name__ == "__main__":
    flet.app(target=main)
