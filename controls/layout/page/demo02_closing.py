import flet
from flet import AlertDialog, Page, Text


def main(page: Page):
    page.title = 'Cierre Aplicación'

    def window_event(event):
        if event.data == 'close':
            page.dialog = dlg_confirm
            dlg_confirm.open = True
            page.update()
    
    page.window_prevent_close = True
    page.on_window_event = window_event