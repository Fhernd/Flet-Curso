import flet as flt
from flet import *


def main(page: Page):
    page.title = "File Picker"

    def pick_files_result(event: FilePickerResultEvent):
        lbl_archivos_seleccionados.value = (
            ", ".join(map(lambda f: f.name, event.files)) if event.files else "Cancelled!"
        )

        lbl_archivos_seleccionados.update()
    
    fpk_selector_archivos = FilePicker(on_result=pick_files_result)
    lbl_archivos_seleccionados = Text()

    def save_file_result(event: FilePickerResultEvent):
        lbl_archivo_guardado.value = (
            event.files[0].name if event.files else "Cancelled!"
        )

        lbl_archivo_guardado.update()
    
    fpk_guardar_archivo = FilePicker(on_result=save_file_result)
    lbl_archivo_guardado = Text()

    def get_directory_result(event: FilePickerResultEvent):
        lbl_directorio_seleccionado.value = event.path if event.path else "Cancelled!"

        lbl_directorio_seleccionado.update()
    
    fpk_directory_dialog = FilePicker(on_result=get_directory_result)
    lbl_directorio_seleccionado = Text()

    page.overlay.extend([fpk_selector_archivos, fpk_guardar_archivo, fpk_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: fpk_selector_archivos.pick_files(
                        allow_multiple=True
                    ),
                ),
                lbl_archivos_seleccionados,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: fpk_guardar_archivo.save_file(),
                    disabled=page.web,
                ),
                lbl_archivo_guardado,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Open directory",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: fpk_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                lbl_directorio_seleccionado,
            ]
        ),
    )


if __name__ == "__main__":
    flt.app(target=main)
