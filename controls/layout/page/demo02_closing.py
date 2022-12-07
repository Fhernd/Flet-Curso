import flet
from flet import AlertDialog, ElevatedButton, OutlinedButton, Page, Text


def main(page: Page):
    page.title = 'Cierre Aplicación'

    def window_event(event):
        if event.data == 'close':
            page.dialog = dlg_confirm
            dlg_confirm.open = True
            page.update()
    
    page.window_prevent_close = True
    page.on_window_event = window_event

    def yes_clicked(event):
        page.window_destroy()
    
    def no_clicked(event):
        dlg_confirm.open = False
        page.update()
    
    dlg_confirm = AlertDialog(
        title=Text('Por favor confirme'),
        modal=True,
        content=Text('¿Está seguro que desea salir de la aplicación?'),
        actions=[
            ElevatedButton('Sí', on_click=yes_clicked),
            OutlinedButton('No', on_click=no_clicked)
        ])
    
    page.add(Text('Intente salir de esta aplicación usando el botón de cierre.'))


if __name__ == '__main__':
    flet.app(target=main)
