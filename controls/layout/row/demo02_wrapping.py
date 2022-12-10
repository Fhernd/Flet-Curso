import flet
from flet import Column, Container, Page, Row, Slider, Text, border_radius, colors


def main(page: Page):
    page.title = 'Row Demo - Wrapping'

    def generar_items(contador):
        items = []

        for i in range(1, contador + 1):
            items.append(
                Container(
                    content=Text(f'{i}'),
                    alignment=flet.alignment.center,
                    width=50,
                    height=50,
                    border_radius=border_radius.all(5),
                    bgcolor=colors.AMBER
                )
            )
        
        return items
    
    def slider_on_change(evento):
        row_elementos.width = int(evento.control.value)
        row_elementos.update()
    

    sld_ancho = Slider(
        min=0,
        max=page.window_width,
        divisions=20,
        value=page.window_width,
        label='{value}',
        on_change=slider_on_change
    )

    row_elementos = Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=generar_items(30),
        width=page.window_width
    )

    page.add(
        Column([
            Text('Ancho de la fila'),
            sld_ancho,
        ]),
        row_elementos
    )


if __name__ == '__main__':
    flet.app(target=main)
