import PySimpleGUI as sg
import arq_control

def cad_types (user,meio,jan):
    sg.theme('DarkAmber')   

    layout = [ 
                [sg.Text('Cadastro de novo Tipo',font=('Times Roman',30),pad=(0,(20,20)))],              
                [sg.Text('', key="incNAME", visible=True, size=(21,1), pad=(5,(10,0)), text_color='red',font=('Times Roman',11))],
                [sg.Text('Nome:',pad=(5,(0,0)),font=('Times Roman',20)), sg.InputText(key="nome", size=(35,4),pad=(5,(0,0)),font=('Times Roman',12))],        
                [sg.Button('Cadastrar',pad=(30,50),font=('Times Roman',15)), sg.Button('Cancelar',pad=(20,50),font=('Times Roman',15))]
                
            ]


    cad_types = sg.Window(
                    'Treasury Assistant', layout,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='/home/henrique/Documentos/Tesouraria/sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    
    #Nome Inválido
    
    while True:
        event, values = cad_types.read()
            
        if event == 'Cadastrar':            
            
            if(arq_control.consultaTipos(user,meio,values['nome'].upper())):
                cad_types.Element('incNAME').update(value='Nome Inválido')
            else:
                arq_control.criaTipo(user,meio,values['nome'].upper())
                sg.Popup("Novo Tipo Cadastrado!!!")
                cad_types.close()
                jan.un_hide()
                
        if event == 'Cancelar':
            # cad_types.hide()
            cad_types.close()
            jan.un_hide()
            break
        if event==sg.WIN_CLOSED:
            jan.un_hide()
            break
        
    cad_types.close()
