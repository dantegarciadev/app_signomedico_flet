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
  
    def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
            )
            selected_files.update()

            
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

  
    container=ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    [
                        ft.ElevatedButton("procesar SSS",width=300,height=50, bgcolor="#73243D"),
                        #ft.ElevatedButton("procesar txt",width=300,height=50),
                        #ft.ElevatedButton("exportar",width=300,height=50),
                    ],
                    wrap=True,
                    spacing=10,
                    run_spacing=10,
                    width=page.window_width,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),

                ft.Row(
                    [
                        ft.ElevatedButton("procesar SSS",width=300,height=50),
                        ft.ElevatedButton("procesar txt",width=300,height=50,),
                        ft.ElevatedButton("exportar",width=300,height=50),
                        ft.ElevatedButton(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(value="Compound button", size=20),
                                    ],
                            ),
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                            width=300,
                            height=50,
                        ),
                        selected_files,
                        ],
                        ),
                        wrap=True,
                        spacing=10,
                        run_spacing=10,
                        width=page.window_width,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                #
                ft.Row(
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
                
                #
            ],
        ),
        bgcolor="#c4c4c4",
        alignment=ft.alignment.center,     
    )

    page.add(container

    )

ft.app(target=main)