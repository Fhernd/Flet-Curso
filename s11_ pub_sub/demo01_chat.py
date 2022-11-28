import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField


def main(page: Page):
    page.title = "ChatApp"

    def on_message(mensaje):
        col_mensajes.controls.append(Text(mensaje))
        page.update()
    
    page.pubsub.subscribe(on_message)

    def btn_send_click(event):
        page.pubsub.send_all(f'{txt_usuario.value}: {txt_mensaje.value}')
        txt_mensaje.value = ''
        page.update()
    
    col_mensajes = Column()
    txt_usuario = TextField(hint_text='Digite su nombre', width=150)
    txt_mensaje = TextField(hint_text='Digite su mensaje...', expand=True)
    btn_enviar = ElevatedButton('Enviar', on_click=btn_send_click)

    page.add(
        col_mensajes,
        Row(controls=[txt_usuario, txt_mensaje, btn_enviar])
    )


if __name__ == '__main__':
    flet.app(target=main, view=flet.WEB_BROWSER)
