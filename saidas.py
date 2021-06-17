import PySimpleGUI as sg
from config import *
import img 
import cadastro
import arq_control
import tela_principal
import Cad_Types
from objetos import Saida
import functions


def saida (user):
    sg.theme('DarkAmber')   # Add a touch of color
    
    tipos=arq_control.getTypesSAIDA(user.getId())

    layout = [ 
                [sg.Text('Registro de Saída',font=(fonte,30),pad=(0,(50,50)))],
                
                [sg.Text('', key="incVALOR", visible=True, size=(20,1), pad=((110,0),(10,0)), text_color='red',font=(fonte,11))],
                
                [sg.Text('Valor:', pad=(5,(0,0)),font=(fonte,20)), sg.InputText(key="valor", size=(35,1),pad=(5,(0,0)),font=(fonte,12))],
                
                [sg.Text('', key="incTIPO", visible=True, size=(20,1), pad=((30,50),(10,0)), text_color='red',font=(fonte,11)),
                 sg.Text('', key="incDATA", visible=True, size=(20,1), pad=((0,100),(10,0)), text_color='red',font=(fonte,11))],
                
                [sg.Text('Tipo:',font=(fonte,20)), sg.Combo(tipos,size=(18,1), key='tipos', pad=((5,5),(0,0)), font=(fonte,15)),
                 sg.Text('Data:', pad=((10,5),(0,0)),font=(fonte,20)), sg.InputText(key="calendario", visible=False, size=(10,1),pad=(5,(0,0)),font=(fonte,12)), 
                 sg.CalendarButton('', button_color=('black','gray'), image_filename='lupa.png', format = "%d/%m/%y")],
                
                [sg.Button('Registrar', pad=(30,50),font=(fonte,15)), sg.Button('Voltar', pad=(30,50),font=(fonte,15))],
                [sg.Image(data=img.img_1,pad=((0,0),(60,0)))]
            ]


    saida = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    
    # saida.Element('incVALOR').update(visible=False)
    # saida.Element('incDATA').update(visible=False)
    # saida.Element('incTIPO').update(visible=False)


    #Valor Inválido
    #Tipo não Selecionado
    #Data inválida

    while True:
        aval=[0,0,0]
        event, values = saida.read()
        if event == 'Registrar': 
            try: 
                if(float(values['valor'])<=0):
                    saida.Element('incVALOR').update(value='Valor Inválido')
                    aval[0]=1                       
                else:
                    saida.Element('incVALOR').update(value='')    
                    aval[0]=0             
            except:
                saida.Element('incVALOR').update(value='Valor Inválido')
                aval[0]=1
            else:
                saida.Element('incVALOR').update(value='')   
                aval[0]=0    
                
            if(functions.analiseData(values['calendario'])):
                saida.Element('incDATA').update(value='')   
                aval[1]=0               
            else:
                saida.Element('incDATA').update(value='Data inválida')
                aval[1]=1
            
                
            if(values['tipos']==''):
                saida.Element('incTIPO').update(value='Tipo não Selecionado')
                aval[2]=1
            elif(values['tipos']=='CRIAR'):
                saida.hide()
                Cad_Types.cad_types(user,'saida',saida)
                
                tipos=arq_control.getTypesSAIDA(user.getId())
                saida.Element('tipos').update(values=tipos)
                
                saida.Element('incTIPO').update(value='')
                aval[2]=1
            else:
                saida.Element('incTIPO').update(value='')
                aval[2]=0
                
                
            if(aval==[0,0,0]):
                # regis=Entrada(values['valor'],values['tipos'][0],values['nome'],values['calendario'],user)
                try:
                    regis=Saida(values['valor'],values['tipos'],values['calendario'],user)
                except:
                    sg.Popup("ERRO ao registrar :(")                    
                else:
                    sg.Popup("Registro realizado com sucesso!!!") 
                    saida.close()
                    tela_principal.tela_principal(user)      
                 
        if event == 'Voltar':
            saida.close()
            tela_principal.tela_principal(user)
        if event==sg.WIN_CLOSED:
            break
        
    saida.close()
