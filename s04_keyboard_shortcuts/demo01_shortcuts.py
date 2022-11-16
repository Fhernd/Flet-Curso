import flet
from flet import KeyboardEvent, Page, Text


def main(page: Page):
    def on_keyboard(event: KeyboardEvent):
        page.add(
            Text(
                f'Key: {event.key}, Shift: {event.shift}, Control: {event.ctrl}, Alt: {event.alt}, Meta: {event.meta}'
            )
        )
    
    page.on_keyboard_event = on_keyboard

    page.add(Text('Presione cualquier tecla con una combinación (Control, Alt, Shift, Command)...'))


flet.app(target=main)
