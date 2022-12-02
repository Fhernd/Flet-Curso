import flet
from flet import Checkbox, Column, FloatingActionButton, Page, Row, Text, TextField, UserControl, icons


class ToDoApp(UserControl):
    def build(self):
        self.txt_tarea = TextField(hint_text='¿Qué necesitas hacer?', expand=True)
        btn_agregar_tarea = FloatingActionButton(icon=icons.ADD, on_click=self.btn_agregar_tarea_clicked)

        self.col_tareas = Column()
        col_controles = Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.txt_tarea,
                        btn_agregar_tarea
                    ]
                ),
                self.col_tareas
            ]
        )

        return col_controles
    
    def btn_agregar_tarea_clicked(self, event):
        self.col_tareas.controls.append(Checkbox(label=self.txt_tarea.value))
        self.txt_tarea.value = ''
        self.update()


def main(page: Page):
    
    todo = ToDoApp()

    page.horizontal_alignment = 'center'
    page.add(todo)


flet.app(target=main)
