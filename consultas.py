import PySimpleGUI as sg
from config import *
import img 
import cadastro
import arq_control
import objetos
import entradas
import saidas
import tela_principal
import con_saidas
import con_entradas
import con_geral

def consultas (user):
    sg.theme('DarkAmber')   # Add a touch of color

    layout = [ 
                [sg.Text('Consultas',font=(fonte,30),pad=(0,(50,0)))],
                [sg.Text('Escolha o Setor de busca.',font=(fonte,25), pad=(0,(0,50)))],                                                
                [sg.Button('Entradas', pad=(30,50), font=(fonte,20)), 
                 sg.Button('Saídas',pad=(20,50), font=(fonte,20)), 
                 sg.Button('Geral',pad=(20,50),font=(fonte,20))],
                [sg.Button('Voltar',pad=(20,20),font=(fonte,20))],
                [sg.Image(data=img.img_1,pad=((0,0),(60,0)))]
            ]


    consultas = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()

    while True:
        event, values = consultas.read()
        if event == 'Entradas': 
            pass            
        if event == 'Saídas':
            consultas.close()
            con_saidas.con_saida(user)
        if event == 'Geral':
            pass
        if event == 'Voltar':
            consultas.close()
            tela_principal.tela_principal(user)
        if event==sg.WIN_CLOSED:
            break
        
    consultas.close()
