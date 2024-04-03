import flet as ft
import time
import os
import datetime





def generate_container(img=None, btns_color=ft.colors.RED_50, containers_width=100, 
                       containers_height = 100,  ):
    if img:
        data_path = os.path.join(os.getcwd(), 'img')
        img_container = ft.Image(data_path+'//'+img, height=80, width=80, fit=ft.ImageFit.CONTAIN)


        return ft.Container(
        img_container, 
        width= containers_width, 
        height=containers_height, 
        alignment=ft.alignment.center,
        bgcolor=btns_color, 
        border_radius=10, 
        on_click=lambda e, img=img: on_click_callback(e, img),
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

def on_click_callback(e, img):

    moments.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    requests.append(img)

    for moment, request in zip(moments, requests):
        print(f'{moment} : {request}')

    # page.update()


def main(page: ft.Page):

    global requests
    global moments
    moments = []
    requests = []

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text('Haptic vest control app'),
        center_title=True,
        color=ft.colors.BLACK87,
        bgcolor=ft.colors.INDIGO_200,
    )

    flechas_text = [ None , 'Arriba.png', None, 'Izquierda.png', None, 'Derecha.png', 'Abajo.png']
    flechas_container = [generate_container(img) for img in flechas_text]
    arrows = ft.ResponsiveRow(
        controls=flechas_container
        , alignment=ft.MainAxisAlignment.CENTER, spacing=8)
    page.bgcolor = ft.colors.DEEP_PURPLE_100

    page.add(arrows)

    petitions  = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    petitions_table = ft.ResponsiveRow(
        controls=[petitions],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8,

    )
    

    page.add(petitions_table)


ft.app(target=main)