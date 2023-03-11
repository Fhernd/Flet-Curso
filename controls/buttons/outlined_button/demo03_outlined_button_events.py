import flet as flt
from flet import *


def main(page: Page):
    page.title = "Outlined Button - Demostración con eventos"

    def on_click(event):
        obn_generador_evento.data += 1
        lbl_resultado.value = f'Has hecho click {obn_generador_evento.data} veces'
        page.update()

    obn_generador_evento = OutlinedButton('Button with `click` event', on_click=on_click, data=0)
    lbl_resultado = Text('Has hecho click 0 veces')

    page.add(obn_generador_evento, lbl_resultado)


if __name__ == '__main__':
    flt.app(target=main)
