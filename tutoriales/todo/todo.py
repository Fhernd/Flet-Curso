import flet
from flet import Checkbox, FloatingActionButton, Page, Text, TextField, icons


def main(page: Page):

    def btn_agregar_tarea_clicked(event):
        page.add(
            Checkbox(label=txt_tarea.value)
        )
        txt_tarea.value = ''
        page.update()
    
    txt_tarea = TextField(hint_text='¿Qué necesitas hacer?')
    btn_agregar_tarea = FloatingActionButton(icon=icons.ADD, on_click=btn_agregar_tarea_clicked)

    page.add(
        txt_tarea,
        btn_agregar_tarea
    )



flet.app(target=main)
