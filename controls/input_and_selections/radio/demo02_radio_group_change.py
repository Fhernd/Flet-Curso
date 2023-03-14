import flet as flt
from flet import *


def main(page: Page):
    page.title = "Radio"

    def rgp_colores_changed(event):
        lbl_estado.value = f'Su color favorito es: {event.control.value}'

        page.update()
    
    lbl_estado = Text()

    rgp_colores = RadioGroup(
        content=Column([
            Radio(label='Rojo', value='Rojo'),
            Radio(label='Verde', value='Verde'),
            Radio(label='Azul', value='Azul'),
        ]),
        on_change=rgp_colores_changed
    )

    page.add(Text('¿Cuál es tu color favorito?'))
    page.add(rgp_colores)
    page.add(lbl_estado)


if __name__ == '__main__':
    flt.app(target=main)
