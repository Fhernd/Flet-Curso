import flet as flt
import flet import *


def main(page: Page):

    def page_resize(event):
        lbl_ancho.value = f'{page.width}px'
        lbl_ancho.update()
    
    page.on_resize = page_resize

    lbl_ancho = Text(bottom=50, rigth=50, style='displaySmall')

    page.overlay.append(lbl_ancho)


