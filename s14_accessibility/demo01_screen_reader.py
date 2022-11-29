import flet
from flet import FloatingActionButton, KeyboardEvent, Page, Text, icons
from flet import Main


def main(page: Page):
    page.title = "Screen Reader"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    def on_keyboard(event: KeyboardEvent):
        if event.key == 'S' and event.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()
