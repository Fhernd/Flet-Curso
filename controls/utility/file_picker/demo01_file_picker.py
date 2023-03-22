import flet as flt
from flet import *


def main(page: Page):
    page.title = "File Picker"

    def pick_files_result(event: FilePickerResultEvent):
        lbl_archivos_seleccionados.value = (
            ", ".join(map(lambda f: f.name, event.files)) if event.files else "Cancelled!"
        )

        lbl_archivos_seleccionados.update()
    
    fpk_archivos = FilePicker(on_result=pick_files_result)
    lbl_archivos_seleccionados = Text()

    page.overlay.append(fpk_archivos)

    page.add(
        Row([
            ElevatedButton(
                "Pick files",
                icon=icons.UPLOAD_FILE,
                on_click=lambda _: fpk_archivos.pick_files(
                    allow_multiple=True
                ),
            ),
            lbl_archivos_seleccionados
        ])
    )


if __name__ == "__main__":
    flt.app(target=main)
