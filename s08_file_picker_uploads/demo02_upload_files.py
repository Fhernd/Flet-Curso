from typing import Dict

import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons
)
from flet.column import Column


def main(page: Page):
    barras_progreso: Dict[str, ProgressRing] = {}
    archivos = Ref[Column]()
    btn_subir = Ref[ElevatedButton]()

    def file_picker_result(event: FilePickerResultEvent):
        btn_subir.current.disabled = True if event.files is None else False
        barras_progreso.clear()
        archivos.current.controls.clear()

        if event.files is not None:
            for f in event.files:
                pbr_archivo = ProgressRing(value=0, bgcolor='#eeeeee', width=20, height=20)
                barras_progreso[f.name] = pbr_archivo
                archivos.current.controls.append(Row([pbr_archivo, Text(f.name)]))
        
        page.update()
    
    def on_upload_progress(event: FilePickerUploadEvent):
        barras_progreso[event.file_name].value = event.progress
        barras_progreso[event.file_name].update()
    
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(event):
        lista_archivos = []

        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                lista_archivos.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600)
                    )
                )
            
            file_picker.upload(lista_archivos)
    
    page.overlay.append(file_picker)

    page.add(
        ElevatedButton(
            'Seleccionar archivos...',
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True)
        ),
        Column(ref=archivos),
        ElevatedButton(
            'Subir',
            ref=btn_subir,
            icon=icons.UPLOAD,
            on_click=upload_files,
            disabled=True
        )
    )


flet.app(target=main, upload_dir='uploads')
