import flet as flt
from flet import *


def main(page: Page):

    def page_resize(event):
        lbl_ancho.value = f'{page.width}px'
        lbl_ancho.update()
    
    page.on_resize = page_resize

    lbl_ancho = Text(bottom=50, right=50, style='displaySmall')

    page.overlay.append(lbl_ancho)

    rrw_columnas = ResponsiveRow([
        Container(
            Text('Columna 1'),
            padding=5,
            bgcolor=colors.YELLOW,
            col={'sm': 6, 'md': 4, 'xl': 2}
        ),
        Container(
            Text('Columna 2'),
            padding=5,
            bgcolor=colors.GREEN,
            col={'sm': 6, 'md': 4, 'xl': 2}
        ),
        Container(
            Text('Columna 3'),
            padding=5,
            bgcolor=colors.BLUE,
            col={'sm': 6, 'md': 4, 'xl': 2}
        ),
        Container(
            Text('Columna 4'),
            padding=5,
            bgcolor=colors.PINK_300,
            col={'sm': 6, 'md': 4, 'xl': 2}
        )
    ])

    rrw_campos = ResponsiveRow([
        TextField(label='Campo 1', col={'sm': 4}),
        TextField(label='Campo 2', col={'sm': 4}),
        TextField(label='Campo 3', col={'sm': 4}),
    ], run_spacing={'xs': 10})

    page.add(rrw_columnas, rrw_campos)

    page_resize(None)


if __name__ == '__main__':
    flt.app(target=main)
