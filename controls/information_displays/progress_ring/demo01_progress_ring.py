from time import sleep

import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Progress Ring Demo'

    prr_simple = ProgressRing()

    lbl_indicador_lineal = Text('Indicador de progreso circular', style='headlineSmall')

    row_texto = Row([
        Text('Realizando una tarea...'),
    ])

    lbl_indicador_indeterminado = Text('Indicador de progreso circular indeterminado', style='headlineSmall')

    col_operacion = Column([
        ProgressRing(),
        Text('Un proceso que puede tardar un eón...')
    ],
    horizontal_alignment='center')

    page.add(lbl_indicador_lineal)
    page.add(row_texto)
    page.add(prr_simple)
    page.add(lbl_indicador_indeterminado)
    page.add(col_operacion)

    for i in range(0, 101):
        prr_simple.value = i * 0.01
        sleep(0.1)
        page.update()


if __name__ == '__main__':
    flt.app(target=main)
