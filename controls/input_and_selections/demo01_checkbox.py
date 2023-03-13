import flet as flt
from flet import *


def main(page: Page):
    page.title = "Input and Selections"

    def btn_clicked(event):
        lbl_estado.value = (
            f'Estados: {chk_1.value}, {chk_2.value}, {chk_3.value}, {chk_4.value}, {chk_5.value}'  
        )

        page.update()
    
    lbl_estado = Text()

    chk_1 = Checkbox(label='Unchecked by default checkbox', value=False)
    chk_2 = Checkbox(label='Checked by default tristate checkbox', tristate=True)
    chk_3 = Checkbox(label='Checked by default checkbox', value=True)
    chk_4 = Checkbox(label='Disabled checkbos', disabled=True)
    chk_5 = Checkbox(label="Checkbox with rendered label_position='left'", label_position='left')

    btn = ElevatedButton(text='Submit', on_click=btn_clicked)

    page.add(
        chk_1,
        chk_2,
        chk_3,
        chk_4,
        chk_5,
        btn,
        lbl_estado
    )


if __name__ == '__main__':
    flt.app(target=main)
