import time

import flet
from flet import AnimatedSwitcher, ElevatedButton, Image, Page


def main(page: Page):

    imagen = Image(src="https://picsum.photos/150/150", width=150, height=150)

    def animate(event):
        sw.content = Image(
            src=f'https://picsum.photos/150/150?{time.time()}',
            width=150,
            height=150
        )
        page.update()
    
    sw = AnimatedSwitcher(
        imagen,
        transition='scale',
        duration=500,
        reverse_duration=500,
        switch_in_curve='bounceOut',
        switch_out_curve='bounceIn'
    )

    page.add(
        sw,
        ElevatedButton(
            'Animate',
            on_click=animate
        )
    )


# Modo escritorio:
flet.app(target=main)
