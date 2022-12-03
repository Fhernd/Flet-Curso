import flet
from flet import Checkbox, Column, FloatingActionButton, IconButton, Page, Row, Tab, Tabs, Text, TextField, UserControl, colors, icons


class Task(UserControl):
    def __init__(self, nombre_tarea, delete_callback):
        super().__init__()
        self.nombre_tarea = nombre_tarea
        self.delete_callback = delete_callback

    def build(self):
        self.chk_tarea = Checkbox(value=False, label=self.nombre_tarea)
        self.txt_tarea = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.chk_tarea,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(icon=icons.CREATE_OUTLINED, 
                        tooltip='Actualizar tarea',
                        on_click=self.btn_edit_clicked),
                        IconButton(icon=icons.DELETE_OUTLINED,
                        tooltip='Eliminar tarea',
                        on_click=self.btn_delete_clicked)
                    ]
                )
            ]
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.txt_tarea,
                IconButton(icon=icons.DONE_OUTLINE_OUTLINED,
                icon_color=colors.GREEN, 
                tooltip='Actualizar tarea',
                on_click=self.btn_save_clicked)
            ])
        
        return Column(
            controls=[
                self.display_view,
                self.edit_view
            ])
    
    def btn_edit_clicked(self, event):
        self.txt_tarea.value = self.chk_tarea.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
    
    def btn_delete_clicked(self, event):
        self.delete_callback(self)

    def btn_save_clicked(self, event):
        self.chk_tarea.label = self.txt_tarea.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
        

class ToDoApp(UserControl):
    def build(self):
        self.txt_tarea = TextField(hint_text='¿Qué necesitas hacer?', expand=True)
        btn_agregar_tarea = FloatingActionButton(icon=icons.ADD, on_click=self.btn_agregar_tarea_clicked)

        self.col_tareas = Column()

        self.tabs_filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text='Todas'),
                Tab(text='Activas'),
                Tab(text='Completadas')
            ]
        )

        col_controles = Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.txt_tarea,
                        btn_agregar_tarea
                    ]
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.tabs_filter,
                        self.col_tareas
                    ],
                )
            ]
        )

        return col_controles
    
    def tabs_changed(self, event):
        pass
    
    def btn_agregar_tarea_clicked(self, event):
        tarea = Task(self.txt_tarea.value, self.delete_task)
        self.col_tareas.controls.append(tarea)
        self.txt_tarea.value = ''
        self.update()
    
    def delete_task(self, task):
        self.col_tareas.controls.remove(task)
        self.update()

    def update(self):
        status = self.tabs_filter.tabs[self.tabs_filter.selected_index].text

        for t in self.col_tareas.controls:
            t.visible = (
                status == 'Todas' 
                or (status == 'Activas' and True) 
                or (status == 'Completadas' and False)
            )
        
        super().update()

def main(page: Page):
    
    todo = ToDoApp()

    page.horizontal_alignment = 'center'
    page.add(todo)


flet.app(target=main)
