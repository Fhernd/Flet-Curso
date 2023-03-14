import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Dropdown dinámico'

    def find_option(opcion):
        for option in dbx.options:
            if option.key == opcion:
                return option
        
        return None

    def btn_add_clicked(event):
        dbx.options.append(flt.dropdown.Option(txt_name.value))
        dbx.value = txt_name.value
        txt_name.value = ''
        page.update()
    
    def btn_delete_clicked(event):
        option = find_option(dbx.value)
        if option:
            dbx.options.remove(option)
            page.update()
    
    dbx = Dropdown()
    txt_name = TextField(hint_text='Ingrese el nombre del ítem')

    btn_add = ElevatedButton(text='Agregar', on_click=btn_add_clicked)
    btn_delete = ElevatedButton(text='Eliminar', on_click=btn_delete_clicked)

    page.add(
        dbx,
        txt_name,
        btn_add,
        btn_delete
    )


if __name__ == '__main__':
    flt.app(target=main)
