import flet
from flet import ElevatedButton, Page, Row, Text


def main(page: Page):
    page.title = 'Calculadora'
    
    lbl_resultado = Text(value='0')

    page.add(
        Row(controls=[lbl_resultado]),
        Row(controls=[
            ElevatedButton(text='AC'),
            ElevatedButton(text='+/-'),
            ElevatedButton(text='%'),
            ElevatedButton(text='/')
        ]),
        Row(controls=[
            ElevatedButton(text='7'),
            ElevatedButton(text='8'),
            ElevatedButton(text='9'),
            ElevatedButton(text='*')
        ]),
        Row(controls=[
            ElevatedButton(text='4'),
            ElevatedButton(text='5'),
            ElevatedButton(text='6'),
            ElevatedButton(text='-')
        ]),
        Row(controls=[
            ElevatedButton(text='1'),
            ElevatedButton(text='2'),
            ElevatedButton(text='3'),
            ElevatedButton(text='+')
        ]),
        Row(controls=[
            ElevatedButton(text='0'),
            ElevatedButton(text='.'),
            ElevatedButton(text='=')
        ]),
    )


if __name__ == '__main__':
    flet.app(target=main)
