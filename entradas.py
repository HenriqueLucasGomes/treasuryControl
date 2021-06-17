import PySimpleGUI as sg
import img 
import cadastro
import arq_control
import tela_principal
import Cad_Types
from objetos import Entrada
import functions
import logging

def entrada (user):
    sg.theme('DarkAmber')   # Add a touch of color

    tipos=arq_control.getTypesENTRADA(user.getId())

    layout = [ 
                [sg.Text('Registro de Entrada',font=('Times Roman',30),pad=(0,(50,50)))],
                
                [sg.Text('', key="incVALOR", visible=True, size=(20,1), pad=((80,0),(10,0)), text_color='red',font=('Times Roman',11)),
                 sg.Text('', key="incDATA", visible=True, size=(20,1), pad=((50,0),(10,0)), text_color='red',font=('Times Roman',11))],
                
                [sg.Text('Valor:', pad=(5,(0,0)),font=('Times Roman',20)), sg.InputText(key="valor", size=(35,1),pad=(5,(0,0)),font=('Times Roman',12)),
                 sg.Text('Data:', pad=((5,5),(0,0)),font=('Times Roman',20)), sg.InputText(key="calendario", visible=False, size=(10,1),pad=(5,(0,0)),font=('Times Roman',12)), 
                 sg.CalendarButton('', button_color=('black','gray'), image_filename='lupa.png', format = "%d/%m/%y")],
                
                [sg.Text('', key="incNOME", visible=True, size=(20,1), pad=((250,0),(10,0)), text_color='red',font=('Times Roman',11)),
                 sg.Text('', key="incTIPO", visible=True, size=(20,1), pad=((20,0),(10,0)), text_color='red',font=('Times Roman',11))],
                
                [sg.Text('Nome/Alcunha:',font=('Times Roman',20)), sg.InputText(key="nome",size=(35,1),font=('Times Roman',12)),
                 sg.Text('Tipo:',font=('Times Roman',20)), sg.Combo(tipos,  key='tipos',size=(15,1), font=('Times Roman',15))], #sg.Listbox(tipos,  key='tipos',size=(15,1), font=('Times Roman',15))],
                
                [sg.Button('Registrar', pad=(30,50),font=('Times Roman',15)), sg.Button('Voltar', pad=(30,50),font=('Times Roman',15))],
                [sg.Image(data=img.img_1,pad=((0,0),(60,0)))]
            ]


    entrada = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    
    # entrada.Element('incVALOR','incDATA').update(visible=False)
    # entrada.Element('incDATA').update(visible=False)
    # entrada.Element('incNOME','incTIPO').update(visible=False)
    # entrada.Element('incTIPO').update(visible=False)    

    # entrada.Element('incVALOR','incDATA').update(visible=True)
    # entrada.Element('incDATA').update(visible=True)
    # entrada.Element('incNOME','incTIPO').update(visible=True)
    # entrada.Element('incTIPO').update(visible=True)  


    #Valor Inválido
    #Data inválida
    #Nome Inválido
    #Tipo não Selecionado

    while True:
        aval=[0,0,0,0]
        event, values = entrada.read()
        if event == 'Registrar':
            
            try: 
                if(float(values['valor'])<=0):
                    logging.warning("[>] Valor Negativo")
                    entrada.Element('incVALOR').update(value='Valor Inválido')
                    aval[0]=1                    
                else:
                    logging.info("[>] Valor Aceito")
                    entrada.Element('incVALOR').update(value='')
                    aval[0]=0              
            except:
                logging.warning("[>] Valor Inválido")
                entrada.Element('incVALOR').update(value='Valor Inválido')
                aval[0]=1
            else:
                logging.info("[>] Valor Aceito")
                entrada.Element('incVALOR').update(value='') 
                aval[0]=0      
                
            if(functions.analiseData(values['calendario'])):
                logging.info("[>] Data Aceita")
                entrada.Element('incDATA').update(value='')
                aval[1]=0                
            else:
                logging.warning("[>] Data Inválida")
                entrada.Element('incDATA').update(value='Data inválida')
                aval[1]=1
                
            if(values['nome']==''):
                logging.warning("[>] Nome Inválido")
                entrada.Element('incNOME').update(value='Nome Inválido')
                aval[2]=1
            else:
                logging.info("[>] Nome Aceito")
                entrada.Element('incNOME').update(value='')
                aval[2]=0
            
            if(values['tipos']==''):
                logging.warning("[>] Tipo não Selecionado")
                entrada.Element('incTIPO').update(value='Tipo não Selecionado')
                aval[3]=1
            elif(values['tipos']=='CRIAR'):
                logging.info("[>] Modo de Criação Selecionado")
                entrada.hide()
                Cad_Types.cad_types(user,'entrada',entrada)
                
                tipos=arq_control.getTypesENTRADA(user.getId())
                entrada.Element('tipos').update(values=tipos)
                
                entrada.Element('incTIPO').update(value='')
                aval[3]=1
            else:
                logging.info("[>] Tipo Aceito")
                entrada.Element('incTIPO').update(value='')
                aval[3]=0
                
            if(aval==[0,0,0,0]):
                logging.info("[>] Registro Aceito")
                # regis=Entrada(values['valor'],values['tipos'][0],values['nome'],values['calendario'],user)
                try:
                    regis=Entrada(values['valor'],values['tipos'],values['nome'],values['calendario'],user)
                except:
                    logging.error("[>] Registro Falhou!!!")
                    # logging.warning(values['valor']+','+values['tipos']+','+values['nome']+','+values['calendario'])
                    sg.Popup("ERRO ao registrar :(")                    
                else:
                    logging.info("[>] Registro Realizado!!!")
                    sg.Popup("Registro realizado com sucesso!!!") 
                    entrada.close()
                    tela_principal.tela_principal(user)  
                          
        if event == 'Voltar':
            logging.info("[>] Voltando para a Tela Inicial...")
            entrada.close()
            tela_principal.tela_principal(user)
        if event==sg.WIN_CLOSED:
            logging.info("[>] Tela Fechada")
            break
        
    entrada.close()
