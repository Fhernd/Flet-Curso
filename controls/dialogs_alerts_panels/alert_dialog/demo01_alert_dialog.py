import flet as flt
from flet import *


def main(page: Page):
    page.title = "Dialogs, Alerts and Panels"

    dlg_principal = AlertDialog(
        title=Text('¡Hola!'),
        on_dismiss=lambda event: print('Dialogo principal cerrado'),
    )

    def dialog_closed(event):
        dlg_modal.open = False
        page.update()
    
    dlg_modal = AlertDialog(
        modal=True,
        title=Text('Por favor, confirmar'),
        content=Text('¿Está seguro de que desea continuar?'),
        actions=[
            TextButton(text='Sí', on_click=dialog_closed),
            TextButton(text='No', on_click=dialog_closed),
        ],
        actions_alignment='end',
        on_dismiss=lambda event: print('Dialogo modal cerrado'),
    )

    def dialog_open(event):
        page.dialog = dlg_principal
        dlg_principal.open = True
        page.update()
    
    def dlg_modal_open(event):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    btn_abrir_dialog = ElevatedButton(text='Abrir dialogo', on_click=dialog_open)
    btn_abrir_dialog_modal = ElevatedButton(text='Abrir dialogo modal', on_click=dlg_modal_open)

    page.add(
        btn_abrir_dialog,
        btn_abrir_dialog_modal,
    )


if __name__ == '__main__':
    flt.app(target=main)
