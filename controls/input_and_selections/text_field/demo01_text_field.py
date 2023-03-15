import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Text Field"

    def btn_guardar_clicked(event):
        lbl_estado.value = f'Valores de los campos de texto: {txt_1.value}, {txt_2.value}, {txt_3.value}, {txt_4.value}, {txt_5.value}' 

        page.update()
    

    lbl_estado = Text()

    txt_1 = TextField(label='Standard')
    txt_2 = TextField(label='Disabled', disabled=True, value='First Name')
    txt_3 = TextField(label='Read-only', read_only=True, value='Last Name')
    txt_4 = TextField(label='With placeholder', hint_text='Please enter text here')
    txt_5 = TextField(label="With an icon", icon=icons.EMOJI_EMOTIONS)

    btn_guardar = ElevatedButton(text='Submit', on_click=btn_guardar_clicked)

    page.add(
        txt_1,
        txt_2,
        txt_3,
        txt_4,
        txt_5,
        btn_guardar,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
