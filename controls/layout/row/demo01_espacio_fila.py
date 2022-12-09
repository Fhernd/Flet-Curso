import flet
from flet import Column, Container, Page, Row, Slider, Text, colors, border_radius


def main(page: Page):
    page.title = 'Row Demo - Espacio entre filas'

    def items(contador):
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
    
    def gap_slider_on_change(evento):
        row_containers.spacing = int(evento.control.value)
        row_containers.update()
    
    sld_espacio = Slider(
        min=0,
        max=50,
        divisions=50,
        value=0,
        label='{value}',
        on_change=gap_slider_on_change)
    
    row_containers = Row(spacing=0, controls=items(10))

    page.add(
        Column([
            Text('Espacio entre ítems'),
            sld_espacio,
        ]),
        row_containers
    )


if __name__ == '__main__':
    flet.app(target=main)
