import flet
from flet import FloatingActionButton, KeyboardEvent, Page, Text, icons


def main(page: Page):
    page.title = "Screen Reader"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def on_keyboard(event: KeyboardEvent):
        if event.key == 'S' and event.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()

    page.on_keyboard_event = on_keyboard

    lbl_numero = Text('10', size=40)

    def btn_incrementar_click(event):
        lbl_numero.value = str(int(lbl_numero.value) + 1)
        lbl_numero.update()
        page.update()
    
    btn_incrementar = FloatingActionButton(
        icon=icons.ADD,
        on_click=btn_incrementar_click,
        tooltip='Incrementa el valor numérico'
    )

    page.add(
        lbl_numero,
        Text('Presione la combinación de teclas Ctlr + S para activar el lector de pantalla'),
        btn_incrementar
    )


if __name__ == '__main__':
    flet.app(target=main)
