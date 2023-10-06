import pandas as pd
import numpy as pd
import flet as ft
from flet import *


def main(page: Page):
    page.appbar=ft.AppBar(
        title=ft.Text("SIGNO MEDICO", italic=True),center_title=True,

    )
    row = ft.Row(
    wrap=True,
    spacing=10,
    run_spacing=10,
    width=page.window_width,
    bgcolor=ft.colors.YELLOW
    )
    page.title="SIGNO MEDICO"
    page.bgcolor = "#c4c4c4"
    page.add(ft.Text("HOLAA FLET"),
             row
        )

ft.app(target=main)