import flet
from flet import Column, Container, Page, Slider, Text, border_radius, colors, alignment


def main(page: Page):
    page.title = "Column Spacing"

    def generar_items(n):
        items = []

        for i in range(1, n + 1):
            items.append(
                Container(
                    content=Text(value=f"{i}"),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER,
                    width=50,
                    height=50,
                    border_radius=border_radius.all(5)
                )
            )
        
        return items
    
    def sld_spacing_change(event):
        col_items.spacing = int(event.control.value)
        col_items.update()
    
    sld_spacing = Slider(
        min=0,
        max=100,
        divisions=10,
        value=0,
        label="{value}",
        width=500,
        on_change=sld_spacing_change
    )
    
    col_items = Column(spacing=0, controls=generar_items(5))

    page.add(
        Column([Text('Espacio entre elementos'), sld_spacing]),
        col_items
    )


if __name__ == "__main__":
    flet.app(target=main)
