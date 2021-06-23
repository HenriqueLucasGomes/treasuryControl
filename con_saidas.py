import PySimpleGUI as sg
from config import *
import img 
import functions
import cadastro
import arq_control
import tela_principal
import filtros
import consultas
import preferencias

def con_saida (user):
    sg.theme('DarkAmber')   # Add a touch of color

    filt={'VAL1': '', 'VAL2': '', 'inicioDATA': '', '': '', 'fimDATA': '', '0': '', 'tipos': []}
    prefere={'data':'1','dataT':'D','valor':'2','valorT':'C','nome':'3','nomeT':'C'}
    busca=list()
    
    # if(filt=={'VAL1': '', 'VAL2': '', 'inicioDATA': '', '': '', 'fimDATA': '', '0': '', 'tipos': []}):
    #     busca=["Filtros não selecionados"]
        
        

    layout = [ 
                [sg.Text('Saídas',font=(fonte,30),pad=(0,(20,0)))],                                
                [sg.Button('Voltar', pad=(10,(30,20)),font=(fonte,15)), 
                 sg.Button('Buscar',pad=(10,(30,20)),font=(fonte,15)),
                 sg.Button('Filtros',pad=(10,(30,20)),font=(fonte,15)),
                 sg.Button('Preferências',pad=(10,(30,20)),font=(fonte,15))],
                [sg.Listbox(busca, text_color='red', key='LISTA', pad=(0,(0,0)), size=(100,19), font=(fonte,15))],
                [sg.Button(image_filename='seta_ESQ.png', visible=False, pad=(0,(0,0)),font=(fonte,15)),
                 sg.Text('1/2',font=(fonte,10), visible=False,),
                 sg.Button(image_filename='seta_DIR.png', visible=False,pad=(0,(0,0)),font=(fonte,15))],
            ]


    con_saida = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    


    while True:
        event, values = con_saida.read()
        if event == 'Filtros': 
            con_saida.hide()
            filt=filtros.filtros(user,'saida',filt)   
            print(filt)       
            con_saida.un_hide()
            
        if event == 'Preferências': 
            con_saida.hide()
            prefere=preferencias.prefer(user,'saida',prefere)   
            print(prefere)       
            con_saida.un_hide()
                
        if event == 'Buscar':
            s=list()
            busca=arq_control.buscaSaidas(user, filt)
            
            if(busca==[]):
                s=['Nenhum registro encontrado!']
            else:
                busca=functions.ordenaBusca(prefere,busca)
                for i in busca: s.append(str(i.getData())+"  "+str(i.getValor()))
  
            con_saida.Element('LISTA').update(values= s)
            # print(busca[0].getTipo(),busca[1].getTipo(),busca[2].getTipo())
        
        if event == 'Voltar':
            con_saida.close()
            consultas.consultas(user)                
        
        if event==sg.WIN_CLOSED:
            break
        
    con_saida.close()
