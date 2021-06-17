import PySimpleGUI as sg
from config import *
import img 
import cadastro
import arq_control
import tela_principal
import filtros
import consultas

def con_entrada (user,filt):
    sg.theme('DarkAmber')   # Add a touch of color

    layout = [ 
                [sg.Text('Saídas',font=(fonte,30),pad=(0,(30,0)))],
                
                [sg.Button('Buscar',pad=(30,(30,20)),font=(fonte,15))],
                [sg.Button('Voltar', pad=(10,0),font=(fonte,15)), sg.Button('Filtros',pad=(10,0),font=(fonte,15))],
            ]


    con_entrada = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    


    while True:
        event, values = con_entrada.read()
        if event == 'Filtros': 
            con_entrada.hide()
            filt=filtros.filtros(user,'entrada',filt)          
            con_entrada.un_hide()    
        
        if event == 'Buscar':
            pass
        
        if event == 'Voltar':
            con_entrada.close()
            consultas.consultas(user)                
        
        if event==sg.WIN_CLOSED:
            break
        
    con_entrada.close()
