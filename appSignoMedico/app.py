import flet as ft
from flet import IconButton, Page, Row, TextField, icons, colors, Text, ElevatedButton

#reammos la funcion mail para que corra la app.
def main(page: Page):
    page.title = 'Convenios SignoMedico'
    page.vertical_alignment = 'center'
    #cambiar el color de fondo 
    #page.bgcolor = '#9f2a36' usando un color en hexagesimal
    #page.bgcolor = ft.colors.AMBER_400   usando un color desde el modulo colors.
    
    
    
    ingresarValor = TextField(label='Ingrese un valor ')
    txt_number = TextField(
        value='0', # Valor inicial
        text_align='right', # Alinear el texto a la derecha
        width=100, # Establecer el ancho del campo
        bgcolor='#9f2a36', # Establecer el color de fondo usando hexadecimal
        color='#e7eaff' # Establecer el color del texto usando hexadecimal
    )
    
    def actClick(event):
        # Intentar convertir el valor ingresado a un entero
        try:
            number = int(ingresarValor.value)
            # Actualizar el campo de número con el valor ingresado
            txt_number.value = f'{number}'
        # Si ocurre un error, mostrar un mensaje de error y pedir un valor válido
        except ValueError:
            print('Error: el valor ingresado no es un número válido.')
            print('Por favor, ingrese un número entero.')
    
    row2 = Row(controls=[
        ingresarValor,
        ElevatedButton(text='definir', on_click=int(actClick))
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