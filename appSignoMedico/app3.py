import flet as ft
from flet import IconButton, Page, Row, TextField, icons, colors, Text, ElevatedButton, DataTable
import pandas as pd
import numpy as np
import xlrd
import openpyxl


def main(page: ft.Page):
    page.title = 'Convenios SignoMedico'
    page.vertical_alignment = 'center'
    page.bgcolor= '#DBDBDB'
    table = ft.DataTable() # Crear un widget de tabla vacío


    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        
        #guardar el archivo en un dataframe
        if e.files:
            file = e.files[0] # Asumir que solo hay un archivo seleccionado
            meplife = pd.read_excel(file.path, engine='openpyxl') # Leer el archivo como un dataframe de pandas
            
             # Agregar el siguiente código para mostrar los primeros registros en la app
            table.data= meplife.head().to_dict('records') # Convertir las primeras filas del dataframe en una lista de diccionarios

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allowed_extensions=['csv','txt','xls','xlsx'],
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        table # Agregar la tabla a la página
    )
    

ft.app(target=main)