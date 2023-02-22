from time import sleep
import flet as flt
from flet import Page, ListView, Text


def main(page: Page):
    page.title = 'Scrolling automático'

    lvw_lista = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    contador = 1

    for _ in range(60):
        lvw_lista.controls.append(Text(f'Línea {contador}'))
        contador += 1
    
    page.add(lvw_lista)

    for _ in range(60):
        sleep(1)
        lvw_lista.controls.append(Text(f'Línea {contador}'))
        contador += 1
        page.update()


if __name__ == '__main__':
    flt.app(target=main)
