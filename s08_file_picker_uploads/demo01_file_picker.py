import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons
)


def main(page: Page):
    def pick_files_result(event: FilePickerResultEvent):
        selected_files.value = (
            ', '.join(map(lambda f: f.name, event.files)) if event.files else 'CANCELADO'
        )
        selected_files.update()
    
    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    def save_file_result(event: FilePickerResultEvent):
        save_file_path.value = event.path if event.path else 'CANCELADO'
        save_file_path.update()
    
    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    def get_directory_result(event: FilePickerResultEvent):
        directory_path.value = event.path if event.path else 'CANCELADO'
        directory_path.update()
    
    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    'Pick files',
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True)
                ),
                selected_files
            ]
        ),
        Row(
            [
                ElevatedButton(
                    'Save file',
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web
                ),
                save_file_path
            ]
        ),
        Row(
            [
                ElevatedButton(
                    'Open directory',
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web
                ),
                directory_path
            ]
        )
    )


flet.app(target=main)
