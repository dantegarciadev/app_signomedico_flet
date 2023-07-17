import flet as ft
from flet import *
import pandas as pd
import numpy as np

      
            
def headers(df_file : pd.DataFrame) -> list:
    return [ft.DataColumn(ft.Text(header)) for header in df_file.columns]
def rows(df_file : pd.DataFrame) -> list:
    rows = []
    for index, row in df_file.iterrows():
        rows.append(ft.DataRow(cells = [ft.DataCell(ft.Text(row[header])) for header in df_file.columns]))
    return rows

      
    
           
def main(page: ft.Page):
    page.title = 'Convenios SignoMedico'
    page.vertical_alignment = 'center' 
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        file = e.files[0] # Asumir que solo hay un archivo seleccionado
        df_file = pd.read_excel(file.path, engine='openyxl') # Leer el archivo como un dataframe de pandas
        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_files = ft.Text()
        page.overlay.append(pick_files_dialog)
        datatable = ft.DataTable(
            columns=headers(df_file),
            rows=rows(df_file))  




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
            alignment='center'
        ),
        datatable
    )
    

ft.app(target=main)