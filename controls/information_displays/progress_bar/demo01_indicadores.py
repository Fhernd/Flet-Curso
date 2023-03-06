from time import sleep
import flet as flt
from flet import *


def main(page: Page):
    page.title = "Progress Bar - Ejemplo"

    pbr_simple = ProgressBar()

    lbl_indicador_lineal = Text('Indicador de progreso linea', style='headlineSmall')
    col_operacion = Column([
        Text('Realizando una tarea...'),
        pbr_simple,
    ])
    lbl_indicador_indeterminado = Text('Indicador de progreso indeterminado', style='headlineSmall')
    pbr_indeterminado = ProgressBar(width=400, color="amber", bgcolor="#eeeeee")

    page.add(lbl_indicador_lineal)
    page.add(col_operacion)
    page.add(lbl_indicador_indeterminado)
    page.add(pbr_indeterminado)

    for i in range(0, 101):
        pbr_simple.value = i * 0.01
        sleep(0.1)
        page.update()


if __name__ == '__main__':
    flt.app(target=main)
