from time import sleep
import flet
from flet import ElevatedButton, Page, ProgressBar


def main(page: Page):
    page.title = 'Splash Screen'

    def on_show_splash_clicked(event):
        page.splash = ProgressBar()
        btn_show_splash.disabled = True
        page.update()
        sleep(5)

        page.splash = None
        btn_show_splash.disabled = False
        page.update()
    
    btn_show_splash = flet.ElevatedButton('Mostrar Splash Screen', on_click=on_show_splash_clicked)

    page.add(btn_show_splash)


if __name__ == '__main__':
    flet.app(target=main)
