#flet slider app 
#modulos
import flet
from flet import *



def main(page: Page):
    
    #Funcion minimizar
    def _min(e):
        _b.controls[0].width =110
        _b.controls[0].scale = transform.Scale(0.9, alignment.center_right)
        _b.controls[0].border_radius = border_radius.only(
            top_right=0, bottom_right=0,top_left=35,bottom_left=35,
        )
        
        #desabilitar
        _b.controls[0].disabled =True
        _b.controls[0].update()
        pass
    
    
    _a=Container(
        width=300,
        height=550,
        bgcolor="#900b04",
        border_radius=35,
    )
    
    _card_container=Row(scroll="auto")
    
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
                                col={"xs": 8},
                                no_wrap=True, #se setea a verdadero asi se puede crear el efecto slider despues
                                size=20,
                                weight="bold", 
                                color= "#ffffff",
                            ),
                            Container(
                                col={"xs":2},
                                on_click=lambda e: _min(e),
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
                ),
                Container(
                    padding=padding.only(top=10,bottom=20),
                    content=_card_container,   
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
    
    #_card_container
    
    l=["convenio1","convenio2","convenio2"]
    t=["transformar1","transformar2","transformar3"]
    p=[90,123,45]
   
    
    for index in range(3):
        _=Card(elevation=15,
               content=Container(
                   width=160,
                   height=100,
                   padding=15,
                   content=Column(
                        #Muestra seteable UI => para ser modificada despues
                        alignment="spaceBetween",
                        controls=[
                            Container(
                                content=Column(
                                    spacing=3,
                                    controls=[
                                        Text(
                                            #tomo los elementos del index
                                            t[index],
                                            color="white60",
                                            size=12,
                                        ),
                                        Text(
                                            #aca igual
                                            l[index],
                                            size=20,
                                        ),
                                    ],
                                    
                                )
                            ),
                            #se puede usar como la barra de progreso
                            Container(
                                width=160,
                                height=5,
                                bgcolor="white12",
                                border_radius=20,
                                padding=padding.only(right=p[index]),
                                content=Container(
                                    bgcolor="pink",
                                ),
                            ),
                        ],
                   )
               ),
            )
        
        
        _card_container.controls.append(_)
    
    
    
    
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
                _a,
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
    