#flet slider app 
#modulos
import flet
from flet import *



def main(page: Page):
    
    #controles del dashboard
    _top = Container(
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#111827", "#1f2937"],
        ),
        border_radius=30,
        padding = padding.only(top=15,left=15),
        content=Column(
            controls=[
                Container(
                    content=ResponsiveRow(
                        alignment="spaceBetween",
                        controls=[
                            Text(
                                "Signo Medico",
                                col={"xs": 6},
                                no_wrap=True, #se setea a verdadero asi se puede crear el efecto slider despues
                                size=20,
                                weight="bold", 
                                color= "#ffffff",
                            ),
                            Container(
                                col={"xs":1},
                                content=Text(
                                    'ⓘ',
                                    weight='bold', no_wrap=True,
                                    color= "#ffffff",
                                ),
                            ),
                        ]
                    )
                ),
                Container(padding=padding.only(top=20)),
                Text(
                    'CATEGORIES',
                    size=12,
                    color="white60",
                    no_wrap=True,
                    
                )
            ]
            
        ),
    )
    
    #contenedor TOP
    _b = Row(
        alignment='end',
        controls=[
            Container(
                width=300,
                height=500,
                bgcolor="#475569",
                border_radius=35,
                #animaciones
                animate=animation.Animation(duration=500,
                                            curve="decelerate"),
                # Escala => reducir ligeramente el tamanio
                scale= transform.Scale(1, alignment.center_right),
                animate_scale=animation.Animation(duration=500,
                                                  curve="decelerate"),
                padding=5,
                content=Column(
                    controls= [_top,]
                )
                
            )
        ],
    )
    
    #contenedor prinpal
    _c = Container(
        width = 300,
        height= 550,
        bgcolor="grey",
        border_radius=35,
        #Stack es para superponer hijos uno sobre el otro.
        content=Stack(
            width=300,
            height=550,
            controls=[
                _b,
            ]
            
        )
    )
    
    page.add(
        _c
    )
    
    pass

if __name__ == '__main__':
    flet.app(target=main)
    