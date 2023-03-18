import flet as flt
from flet import *


class Data:
    def __init__(self) -> None:
        self.counter = 0


data = Data()


def main(page: Page):
    page.title = "Snackbar"

    page.snack_bar = SnackBar(
        content=Text('Hola, a todos'),
        action='Alright!',
    )

    def on_click(event):
        page.snack_bar = SnackBar(Text(f'Hola, {data.counter}'))
        page.snack_bar.open = True
        data.counter += 1
        page.update()
    
    page.add(
        ElevatedButton('Open Snackbar', on_click=on_click),
    )
    

if __name__ == '__main__':
    flt.app(target=main)
