import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections - Switch"

    def btn_seleccionar_clicked(event):
        lbl_estado.value = f'Estados: {swt_1.value}, {swt_2.value}, {swt_3.value}, {swt_4.value}' 

        page.update()
    
    lbl_estado = Text()

    swt_1 = Switch(label='Unchecked switch', value=False)
    swt_2 = Switch(label='Checked switch', value=True)
    swt_3 = Switch(label='Disabled switch', disabled=True)
    swt_4 = Switch(label="Switch with rendered label_position='left'", label_position='left')

    btn_seleccionar = ElevatedButton(text='Submit', on_click=btn_seleccionar_clicked)

    page.add(
        swt_1,
        swt_2,
        swt_3,
        swt_4,
        btn_seleccionar,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
