import flet
from flet import Column, ElevatedButton, Page, Text, TextField


def main(page: Page):
    page.title = 'Control Ref'

    txt_first_name = TextField(label='First Name', autofocus=True)
    txt_last_name = TextField(label='Last Name')
    col_controles = Column()

    def btn_click(event):
        col_controles.controls.append(Text(f'Hello, {txt_first_name.value} {txt_last_name.value}'))
        txt_first_name.value = ''
        txt_last_name.value = ''
        page.update()
        txt_first_name.focus()
    
    btn_agregar = ElevatedButton('Add', on_click=btn_click)

    page.add(
        txt_first_name,
        txt_last_name,
        btn_agregar,
        col_controles
    )
    

if __name__ == '__main__':
    flet.app(target=main)
