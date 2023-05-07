import flet as ft
from flet import IconButton, Page, Row, TextField, icons, colors, Text, ElevatedButton

#reammos la funcion mail para que corra la app.
def main(page: Page):
    page.title = 'Convenios SignoMedico'
    page.vertical_alignment = 'center'
    #cambiar el color de fondo 
    #page.bgcolor = '#9f2a36' usando un color en hexagesimal
    #page.bgcolor = ft.colors.AMBER_400   usando un color desde el modulo colors.
    txt_number =  TextField(value ='0', text_align='right', width=100, bgcolor='#9f2a36', color= '#e7eaff' )
    
    ingresarValor = TextField(label='Ingrese un valor ')
    
    row2 = Row(controls=[
        ingresarValor,
        ElevatedButton(text='definir', on_click=int(txt_number.value)),
    ],
               alignment='center'
               )
    page.add(row2)
    #dentro de la funcion mail creamos otra funcion para sumar restar
    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1
        page.update()
    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1
        page.update()
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click)
            ],
            alignment='center'
        )
    )

    

    
    
ft.app(target=main)
#ft.app(target=main, view=ft.WEB_BROWSER)