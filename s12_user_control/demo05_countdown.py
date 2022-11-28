import time
from threading import Thread

import flet
from flet import Page, Text, UserControl


class CountdownControl(UserControl):
    def __init__(self, segundos):
        super().__init__()
        self.segundos = segundos

    def did_mount(self):
        self.running = True
        self.hilo = Thread(target=self.actualizar_temporizador, args=(), daemon=True)
        self.hilo.start()
    
    def will_unmount(self):
        self.running = False
    
    def actualizar_temporizador(self):
        while self.running and self.segundos:
            minutos, segundos = divmod(self.segundos, 60)
            self.lbl_temporizador.value = f"{minutos:02d}:{segundos:02d}"
            self.update()
            time.sleep(1)
            self.segundos -= 1
    
    def build(self):
        self.lbl_temporizador = Text()
        return self.lbl_temporizador


def main(page: Page):
    page.title = "Temporizador"

    page.add(CountdownControl(13), CountdownControl(19))


if __name__ == "__main__":
    flet.app(target=main)
