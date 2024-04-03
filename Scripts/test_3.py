import flet as ft
import random



def main(page:ft.Page):
    page.scroll = True
    items = [str(random.randint(0, 100)) for _ in range(1000)]
    cabeza = ft.Text('Hola, como estas?')
    print(items[0])
    items2 = [ft.Text(i, col={'xl':6, 'sm':3, 'xl':1}) for i in items]
    print(items2[0])    
    print('--------------------------------------------------------------------------------------------------------------------')
    cuerpo = ft.Column(
        controls=[ft.ResponsiveRow(items2)],
        scroll=True,
    )
    print('--------------------------------------------------------------------------------------------------------------------')
    fin = ft.Text('Adios')

    page.add(cabeza, cuerpo, fin)

ft.app(target = main)