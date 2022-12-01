import flet
from flet import Checkbox, Column, FloatingActionButton, Page, Row, Text, TextField, icons


def main(page: Page):

    def btn_agregar_tarea_clicked(event):
        page.add(
            Checkbox(label=txt_tarea.value)
        )
        txt_tarea.value = ''
        page.update()
    
    txt_tarea = TextField(hint_text='¿Qué necesitas hacer?')
    btn_agregar_tarea = FloatingActionButton(icon=icons.ADD, on_click=btn_agregar_tarea_clicked)

    col_tareas = Column()
    col_controles = Column(
        width=600,
        controls=[
            Row(
                controls=[
                    txt_tarea,
                    btn_agregar_tarea
                ]
            ),
            col_tareas
        ]
    )

    page.horizontal_alignment = 'center'
    page.add(
        col_controles
    )



flet.app(target=main)
