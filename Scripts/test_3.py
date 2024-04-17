import flet as ft
import os
import datetime


class CardArrow():

    data_list_controls = []

    def __init__(self, page: ft.Page, path: str):
        self.page = page
        self.path = path
    
    def generate_container(self, img=None, btns_color=ft.colors.LIGHT_BLUE_100, containers_width=100, 
                       containers_height = 100): 
        if img:
            self.path = os.path.join(os.getcwd(), 'img')
            img_container = ft.Image(self.path+'//'+img, height=80, width=80, fit=ft.ImageFit.CONTAIN)

            return ft.Container(
                img_container, 
                width= containers_width, 
                height=containers_height, 
                alignment=ft.alignment.center,
                bgcolor=btns_color, 
                border_radius=10, 
                on_click = lambda e, img=img: self.on_click_callback(e, img),
                col={'xs':4, 'sm':4}
            )
        else:
            return ft.Container( 
                width= containers_width, 
                height=containers_height, 
                alignment=ft.alignment.center,
                bgcolor= '#00FF0000', 
                border_radius=10, 
                col={'xs':4, 'sm':4}
            )
        
    def on_click_callback(self, e, img):

        if len(CardArrow.data_list_controls) == 50:
            CardArrow.data_list_controls.pop(-1)
        CardArrow.data_list_controls.insert(0, ft.Text(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} : {img}', color=ft.colors.WHITE, size=20))
        self.page.update()


class DataColumn():

    def __init__(self, page: ft.Page):
        self.page = page

def main(page: ft.Page):

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text('Haptic vest control app'),
        center_title=True,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.LIGHT_BLUE_100,
    )

    #################################
    flechas_text = [ None , 'Arriba.png', None, 'Izquierda.png', None, 'Derecha.png', 'Abajo.png']
    flechas_container = [CardArrow(page, os.getcwd()).generate_container(img) for img in flechas_text]

    
    arrows = ft.ResponsiveRow(
        controls=flechas_container
        , alignment=ft.MainAxisAlignment.CENTER, spacing=8)
    page.bgcolor = ft.colors.WHITE
    #################################
    data_column = ft.ResponsiveRow(
        controls=[
            ft.Container(
                ft.Text('Data', color=ft.colors.WHITE, size=20),
                width=100,
                height=40,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.LIGHT_BLUE_100,
                border_radius=10,
                col={'xs':12, 'sm':12}
            ), 
            ft.Container(                
                ft.ListView(CardArrow.data_list_controls, height=200),
                width=100,
                height=200,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.LIGHT_BLUE_100,
                border_radius=10,
                col={'xs':12, 'sm':12})
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8
    )

    page.add(arrows, data_column) 

    page.update()


ft.app(main)