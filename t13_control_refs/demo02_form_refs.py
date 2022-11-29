import flet
from flet import Column, ElevatedButton, Page, Ref, Text, TextField


def main(page: Page):
    page.title = 'Control Ref [Ref]'
    first_name =  Ref[TextField]()
    last_name =  Ref[TextField]()
    col_controles = Ref[Column]()

    def btn_click(event):
        col_controles.current.controls.append(Text(f'Hello, {first_name.current.value} {last_name.current.value}'))
        first_name.current.value = ''
        last_name.current.value = ''
        page.update()
        first_name.current.focus()
    
    btn_agregar = Ref[ElevatedButton]()

    page.add(
        TextField(ref=first_name, label='First Name', autofocus=True),
        TextField(ref=last_name, label='Last Name'),
        ElevatedButton('Add', ref=btn_agregar, on_click=btn_click),
        Column(ref=col_controles)
    )


if __name__ == '__main__':
    flet.app(target=main)
