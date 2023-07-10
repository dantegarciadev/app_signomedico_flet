import flet as ft
from flet import *
#importar el excel 
from simpledt import ExcelDataTable, DataFrame
import openpyxl
import pandas as pd

def main(page: ft.Page):
    page.scroll ='auto'
    #conseguir el excel primero
    #dframe = ExcelDataTable(r'C:\Users\zickd\Downloads\UOETSYLRA JUNIO.xlsx', engine='openpyxl')
    dframe = pd.read_excel(r'C:\Users\zickd\Downloads\UOETSYLRA JUNIO.xlsx', engine='openpyxl')
    #mostrar el nombre del archivo
    myexcel = DataFrame(dframe.head(20))
    myexcel = myexcel.datatable
    #para que a tabla sea scroleable horizontalmente
    excel_scroll_col=ft.Column([myexcel],scroll=True)
    excel_scroll_row =ft.Row([excel_scroll_col],scroll="always",expand=1,vertical_alignment=ft.CrossAxisAlignment.START)

    page.add(
excel_scroll_row
    )
    
    
ft.app(target=main)


