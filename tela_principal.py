import PySimpleGUI as sg
import img 
import cadastro
import arq_control
import objetos
import entradas
import saidas
import consultas
import filtros
import logging

def tela_principal (user):
    sg.theme('DarkAmber')   # Add a touch of color

    layout = [ 
                [sg.Text('Tela Principal',font=('Times Roman',30),pad=(0,(50,0)))],
                [sg.Text('Por favor Selecione uma Ação.',font=('Times Roman',25), pad=(0,(0,50)))],                                                
                [sg.Button('Entradas', pad=(30,50), font=('Times Roman',20)), 
                 sg.Button('Saídas',pad=(20,50), font=('Times Roman',20)), 
                 sg.Button('Consultas',pad=(20,50),font=('Times Roman',20))],
                [sg.Image(data=img.img_1,pad=((0,0),(60,0)))]
            ]


    tela_PR = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()

    while True:
        event, values = tela_PR.read()
        if event == 'Entradas':
            logging.info("[>] Entradas acessado") 
            tela_PR.close()
            entradas.entrada(user)                
        if event == 'Saídas':
            logging.info("[>] Saídas acessado")
            tela_PR.close()
            saidas.saida(user) 
        if event == 'Consultas':
            logging.info("[>] Consultas acessado")
            tela_PR.close()
            consultas.consultas(user) 
            # filtros.filtros(user,'saida')
        if event==sg.WIN_CLOSED:
            logging.info("[>] Tela Fechada")
            break
        
    tela_PR.close()
