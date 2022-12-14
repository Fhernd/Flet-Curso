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
                    height=50
                )
            )
        
        return items
    
    def set_column_alignment_horizontal(alineacion):
        return Column([
            Text(alineacion, size=16),
            Container(
                content=Column(generar_items(3), horizontal_alignment=alineacion,
                alignment='start'),
                bgcolor=colors.AMBER_100,
                width=100
            )
        ])
    
    page.add(
        Row(
            [
                set_column_alignment_horizontal('start'),
                set_column_alignment_horizontal('center'),
                set_column_alignment_horizontal('end'),
            ],
            spacing=30,
            alignment='start'
            )
    )
    

if __name__ == "__main__":
    flet.app(target=main)
