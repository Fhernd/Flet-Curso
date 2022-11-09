import flet
from flet import Checkbox, ElevatedButton, Page, Row, TextField


def main(page: Page):
    
    def agregar_tarea_clicked(event):
        page.add(Checkbox(label=txt_nueva_tarea.value))
    
    txt_nueva_tarea = TextField(hint_text='¿Cuál tarea desea agregar?', width=300)

    btn_agregar_tarea = ElevatedButton('Agregar', on_click=agregar_tarea_clicked)

    page.add(Row([txt_nueva_tarea, btn_agregar_tarea]))


# Ejecuta la aplicación en modo escritorio:
flet.app(target=main)
