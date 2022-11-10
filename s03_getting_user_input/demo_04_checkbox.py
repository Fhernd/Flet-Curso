import flet
from flet import Checkbox, Page, Text


def main(page: Page):
    def tarea_checked(event):
        lbl_resultado.value = f'¡Has aprendido a programar! ({chk_tarea.value})'

        page.update()
    
    lbl_resultado = Text()
    chk_tarea = Checkbox(label='Aprender a programar', value=False, on_change=tarea_checked)

    page.add(chk_tarea, lbl_resultado)


# Modo escritorio:
flet.app(target=main)
