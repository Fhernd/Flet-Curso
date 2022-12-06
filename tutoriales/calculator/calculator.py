import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius, colors


class CalculadoraApp(UserControl):
    def build(self):
        self.reset()
        self.lbl_resultado = Text(value='0', color=colors.WHITE, size=20)

        return Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.lbl_resultado], alignment='end'),
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
        data = event.control.data

        if self.lbl_resultado.value == 'Error' or data == 'AC':
            self.lbl_resultado.value = '0'
            self.reset()
        elif data in '0123456789.':
            if self.lbl_resultado.value == '0' or self.operando2:
                self.lbl_resultado.value = data
                self.operando2 = False
            else:
                self.lbl_resultado.value += data
        elif data in '+-*/':
            self.lbl_resultado.value = self.calcular(
                self.operando1,
                float(self.lbl_resultado.value),
                self.operador
            )

            self.operador = data

            if self.lbl_resultado.value == 'Error':
                self.operando1 = '0'
            else:
                self.operando1 = float(self.lbl_resultado.value)
            
            self.operando2 = True
        elif data == '+/-':
            if float(self.lbl_resultado.value) > 0:
                self.lbl_resultado.value = '-' + self.lbl_resultado.value
            elif float(self.lbl_resultado.value) < 0:
                self.lbl_resultado.value = str(self.formatear_numero(abs(float(self.lbl_resultado.value))))
        
        elif data == '%':
            self.lbl_resultado.value = str(float(self.lbl_resultado.value) / 100)
            self.reset()
        
        elif data == '=':
            self.lbl_resultado.value = self.calcular(
                self.operando1,
                float(self.lbl_resultado.value),
                self.operador
            )

            self.reset()
        
        self.update()
    
    def reset(self):
        self.operador = '+'
        self.operando1 = 0
        self.operando2 = True
    
    def formatear_numero(self, numero):
        if numero % 1 == 0:
            return int(numero)
        else:
            return numero

    def calcular(self, operando1, operando2, operador):
        if operador == '+':
            return str(self.formatear_numero(operando1 + operando2))
        elif operador == '-':
            return str(self.formatear_numero(operando1 - operando2))
        elif operador == '*':
            return str(self.formatear_numero(operando1 * operando2))
        elif operador == '/':
            if operando2 == 0:
                return 'Error'
            else:
                return str(self.formatear_numero(operando1 / operando2))


def main(page: Page):
    page.title = 'Calculadora'

    calculadora = CalculadoraApp()

    page.add(calculadora)


if __name__ == '__main__':
    flet.app(target=main)
