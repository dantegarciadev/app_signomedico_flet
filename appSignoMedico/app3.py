import flet as ft
from flet import IconButton, Page, Row, TextField, icons, colors, Text, ElevatedButton, DataTable
import pandas as pd
import numpy as np


def main(page: ft.Page):
    page.title = 'Convenios SignoMedico'
    page.vertical_alignment = 'center'
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        
        #guardar el archivo en un dataframe
        if e.files:
            file = e.files[0] # Asumir que solo hay un archivo seleccionado
            meplife = pd.read_excel(file.path, engine='openpyxl') # Leer el archivo como un dataframe de pandas
            # # Imprimir el dataframe para verificar
            
             # Agregar el siguiente código para mostrar los primeros registros en la app
            table.data= meplife.head(5).to_dict('records') # Convertir las primeras filas del dataframe en una lista de diccionarios
            table.update()
            print(table)
            

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    table = ft.DataTable() # Crear un widget de tabla vacío

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Subir Archivo",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allowed_extensions=['csv','txt','xls','xlsx'],
                        allow_multiple=False,
                        dialog_title='buscar archivo'
                    ),
                ),
                selected_files,
            ],
            alignment='center'
        ),
        table # Agregar la tabla a la página
        
    )
    

ft.app(target=main)