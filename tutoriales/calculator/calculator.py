import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius, colors


class CalculadoraApp(UserControl):
    def build(self):
    
        lbl_resultado = Text(value='0', color=colors.WHITE, size=20)

        return Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[lbl_resultado], alignment='end'),
                    Row(controls=[
                        ElevatedButton(
                            text='AC',
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='AC'
                        ),
                        ElevatedButton(
                            text='+/-',
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='+/-'
                        ),
                        ElevatedButton(
                            text='%',
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='%'
                        ),
                        ElevatedButton(
                            text='/',
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='/'
                        )
                    ]),
                    Row(controls=[
                        ElevatedButton(
                            text='7',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='7'
                        ),
                        ElevatedButton(
                            text='8',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='8'
                        ),
                        ElevatedButton(
                            text='9',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='9'
                        ),
                        ElevatedButton(text='*',
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='*'
                        )
                    ]),
                    Row(controls=[
                        ElevatedButton(
                            text='4',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='4'
                        ),
                        ElevatedButton(
                            text='5',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='5'
                        ),
                        ElevatedButton(
                            text='6',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='6'
                        ),
                        ElevatedButton(
                            text='-',
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='-'
                        )
                    ]),
                    Row(controls=[
                        ElevatedButton(
                            text='1',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='1'
                        ),
                        ElevatedButton(
                            text='2',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='2'
                        ),
                        ElevatedButton(
                            text='3',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='3'
                        ),
                        ElevatedButton(
                            text='+',
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='+'
                        )
                    ]),
                    Row(controls=[
                        ElevatedButton(
                            text='0',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=2,
                            on_click=self.btn_action_clicked,
                            data='0'
                        ),
                        ElevatedButton(
                            text='.',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='.'
                        ),
                        ElevatedButton(
                            text='=',
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                            on_click=self.btn_action_clicked,
                            data='='
                        )
                    ])
                ]
            )
        )
    
    def btn_action_clicked(self, event):
        if event.data == 'AC':
            self.lbl_resultado.value = '0'
        elif event.data == '+/-':
            self.lbl_resultado.value = str(float(self.resultado) * -1)
        elif event.data == '%':
            self.lbl_resultado.value = str(float(self.resultado) / 100)
        elif event.data == '=':
            self.lbl_resultado.value = ''


def main(page: Page):
    page.title = 'Calculadora'

    calculadora = CalculadoraApp()

    page.add(calculadora)


if __name__ == '__main__':
    flet.app(target=main)
