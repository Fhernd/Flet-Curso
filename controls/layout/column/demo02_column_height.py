import flet
from flet import Column, Container, Page, Slider, Text, alignment, border_radius, colors


HEIGHT = 400


def main(page: Page):
    page.title = "Column Height - Slider"

    def generar_items(n):
        items = []

        for i in range(1, n + 1):
            items.append(
                Container(
                    content=Text(f"{i}"),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER,
                    width=30,
                    height=30,
                    border_radius=border_radius.all(5)
                )
            )
        
        return items
    
    def sld_height_change(event):
        col_items.height = int(event.control.value)
        col_items.update()
    
    sld_height = Slider(
        min=0,
        max=HEIGHT,
        divisions=20,
        value=HEIGHT,
        label="{value}",
        width=500,
        on_change=sld_height_change
    )

    col_items = Column(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=generar_items(10),
        height=HEIGHT
    )

    page.add(
        Column(
            [
                Text('Altura de la columna'),
                sld_height
            ]
        ),
        Container(
            content=col_items,
            bgcolor=colors.AMBER_100
        )
    )


if __name__ == "__main__":
    flet.app(target=main)
