import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Elevated Button con Evento Click Demo'

    def btn_contador_clicked(event):
        btn_contador.data += 1
        lbl_conteo.value = f'Has hecho click {btn_contador.data} veces'
        page.update()
    
    btn_contador = ElevatedButton(text='Haz click aquí', on_click=btn_contador_clicked, data=0)

    lbl_conteo = Text('Haz click en el botón para incrementar el contador', style='headlineSmall')


    page.add(btn_contador)
    page.add(lbl_conteo)


if __name__ == '__main__':
    flt.app(target=main)
