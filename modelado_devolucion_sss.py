import pandas as pd
import numpy as pd
import flet as ft
from flet import *


def main(page: Page):
  page.appbar = ft.AppBar(
    title=ft.Text("SIGNO MEDICO", italic=True),
    center_title=True, 
  )
  page.window_max_width=1200
  page.window_max_height=700
  page.title = "SIGNO MEDICO"
  page.bgcolor = "#c4c4c4"
  container=ft.Container(
        top=ft.Row(
            [
                ft.ElevatedButton("procesar SSS",width=300,height=50),
                ft.ElevatedButton("procesar txt",width=300,height=50),
                ft.ElevatedButton("exportar",width=300,height=50),
            ],
            wrap=True,
            spacing=10,
            run_spacing=10,
            width=page.window_width,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        _o=ft.Row(
            [
                ft.ElevatedButton("procesar SSS",width=300,height=50),
                ft.ElevatedButton("procesar txt",width=300,height=50),
                ft.ElevatedButton("exportar",width=300,height=50),
            ],
            wrap=True,
            spacing=10,
            run_spacing=10,
            width=page.window_width,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        buton=ft.Row(
            [
                ft.ElevatedButton("procesar SSS",width=300,height=50),
                ft.ElevatedButton("procesar txt",width=300,height=50),
                ft.ElevatedButton("exportar",width=300,height=50),
            ],
            wrap=True,
            spacing=10,
            run_spacing=10,
            width=page.window_width,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        
    bgcolor=ft.colors.YELLOW,
    alignment=ft.alignment.center,

  )




  page.add(container

  )

ft.app(target=main)