import flet as ft
import pandas as pd

df1 = pd.read_excel(r'C:\Users\zickd\Downloads\1ER TANDA ROCIO (SOLO TITULARES) EPV (CUENTA NUEVA).xlsx', engine='openpyxl') # Leer el archivo como un dataframe de pandas
df=df1.head(10)


def headers(df : pd.DataFrame) -> list:
    return [ft.DataColumn(ft.Text(header)) for header in df.columns]

def rows(df : pd.DataFrame) -> list:
    rows = []
    for index, row in df.iterrows():
        rows.append(ft.DataRow(cells = [ft.DataCell(ft.Text(row[header])) for header in df.columns]))
    return rows

            
def main(page: ft.Page):
    datatable = ft.DataTable(
        columns=headers(df),
        rows=rows(df))
    
    page.add(datatable)

ft.app(target=main)