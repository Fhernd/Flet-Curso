import flet as flt
from flet import *


def main(page: flt.Page):
    page.title = "Animated Switcher Demo"

    c1 = Container(
        Text("Hello!", style=TextThemeStyle.HEADLINE_MEDIUM),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.GREEN,
    )

    c2 = Container(
        Text("Bye!", size=50),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.YELLOW,
    )

    animacion = AnimatedSwitcher(
        c1,
        transition=AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve='bounceOut',
        switch_out_curve='bounceIn',
    )

    def animate(event):
        animacion.content = c2 if animacion.content == c1 else c1
        animacion.update()
    
    page.add(
        animacion,
        ElevatedButton('Animate!', on_click=animate),
    )


if __name__ == "__main__":
    flt.app(target=main)
