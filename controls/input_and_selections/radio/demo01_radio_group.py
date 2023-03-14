import flet as flt
from flet import *


def main(page: Page):
    page.title = "Radio"

    def btn_clicked(event):
        lbl_estado.value = f'Su color favorito es: {rgp_colores.value}'

        page.update()
    
    lbl_estado = Text()
    btn = ElevatedButton(text='Submit', on_click=btn_clicked)

    rgp_colores = RadioGroup(
        content=Column([
            Radio(label='Rojo', value='Rojo'),
            Radio(label='Verde', value='Verde'),
            Radio(label='Azul', value='Azul'),
        ])
    )

    page.add(Text('¿Cuál es tu color favorito?'))
    page.add(rgp_colores)
    page.add(btn)
    page.add(lbl_estado)


if __name__ == '__main__':
    flt.app(target=main)
