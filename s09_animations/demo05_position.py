import flet
from flet import Container, ElevatedButton, Page, Stack


def main(page: Page):
    contenedor_rojo = Container(
        width=50,
        height=50,
        bgcolor='red',
        animate_position=1000
    )
    
    contenedor_verde = Container(
        width=50,
        height=50,
        top=60,
        left=0,
        bgcolor='green',
        animate_position=500
    )
    
    contenedor_azul = Container(
        width=50,
        height=50,
        top=120,
        left=0,
        bgcolor='blue',
        animate_position=1000
    )

    def animate_containers(event):
        contenedor_rojo.top = 20
        contenedor_rojo.left = 200
        
        contenedor_verde.top = 100
        contenedor_verde.left = 40
        
        contenedor_azul.top = 180
        contenedor_azul.left = 100

        page.update()
    
    page.add(
        Stack([contenedor_rojo, contenedor_verde, contenedor_azul], height=250),
        ElevatedButton('Animar', on_click=animate_containers)
    )


# Ejecución de la aplicación en modo escritorio:
flet.app(target=main)
