import PySimpleGUI as sg
from config import *
import arq_control

def filtros (user,meio,default):
    sg.theme('DarkAmber')   
    
    if(meio=='saida'):
        tipos=arq_control.getTypesSAIDA(user.getId())
    elif(meio=='entrada'):
        tipos=arq_control.getTypesENTRADA(user.getId())
    else:
        tipos=['ERRO']

    layout = [ 
                [sg.Text('Filtros',font=(fonte,30),pad=(0,(20,20)))],              
                
                [sg.Text('Dados Incoerentes', key="incLOG", visible=True,  pad=(0,(10,0)), text_color='red',font=(fonte,12))],
                [sg.Text('Valor inválido', key="incVAL1", visible=True, size=(19,1), pad=((155,10),(10,0)), text_color='red',font=(fonte,11)),
                 sg.Text('Valor inválido', key="incVAL2", visible=True, size=(21,1), pad=(0,(10,0)), text_color='red',font=(fonte,11))],                
                
                [sg.Text('Valor:',pad=(5,(0,0)),font=(fonte,20)), sg.InputText(key="VAL1", default_text = default['VAL1'], size=(15,4),pad=(5,(0,0)),font=(fonte,12)),
                 sg.Text('até',pad=(5,(0,0)),font=(fonte,20)),sg.InputText(key="VAL2", default_text = default['VAL2'], size=(15,4),pad=(5,(0,0)),font=(fonte,12))],        
                
                [sg.Text('Data inválida', key="incDATA1", visible=True, size=(21,1), pad=((145,0),(10,0)), text_color='red',font=(fonte,11)),
                 sg.Text('Data inválida', key="incDATA2", visible=True, size=(21,1), pad=(40,(10,0)), text_color='red',font=(fonte,11))],
                
                [sg.Text('Data:',pad=(5,(0,0)),font=(fonte,20)), sg.InputText(key="inicioDATA", visible=False, default_text = default['inicioDATA'], size=(15,4),pad=(5,(0,0)),font=(fonte,12)), 
                 sg.CalendarButton('', button_color=('black','gray'), image_filename='lupa.png', format = "%d/%m/%y"),        
                 sg.Text('até',pad=(5,(0,0)),font=(fonte,20)), sg.InputText(key="fimDATA", visible=False, default_text = default['fimDATA'], size=(15,4),pad=(5,(0,0)),font=(fonte,12)),        
                 sg.CalendarButton('', button_color=('black','gray'), image_filename='lupa.png', format = "%d/%m/%y")],
                
                [sg.Text('Tipo:',font=(fonte,20),pad=(0,(40,0))), sg.Combo(tipos, key='tipos', pad=(0,(40,0)),size=(15,1), font=(fonte,15))],
                # [sg.Listbox(tipos, pad=(0,(40,0)), default_values = default['tipos'], key='tipos',size=(15,1), font=(fonte,15))],
                
                [sg.Button('Filtrar',pad=(30,50),font=(fonte,15)), sg.Button('Cancelar',pad=(20,50),font=(fonte,15))]
                
            ]


    filtros = sg.Window(
                    'Treasury Assistant', layout,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='/home/henrique/Documentos/Tesouraria/sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    
    #Valor inválido
    #Dados Incoerentes
    #Data inválida
    
    while True:
        aval=[0,0]
        event, values = filtros.read()
            
        if event == 'Filtrar': 
             
            if(values['VAL1']=='' and values['VAL2']==''):
                aval[0]=0
                filtros.Element('incVAL1').update(value='')
                filtros.Element('incVAL2').update(value='')
                filtros.Element('incLOG').update(value='')
                
            elif(values['VAL1']!='' and values['VAL2']==''):
                
                aval[0]=1
                filtros.Element('incVAL1').update(value='')
                filtros.Element('incVAL2').update(value='Valor inválido')
                filtros.Element('incLOG').update(value='')
                
                try:
                    if(float(values['VAL1'])<0):
                        filtros.Element('incVAL1').update(value='Valor inválido')
                except:
                    filtros.Element('incVAL1').update(value='Valor inválido')
                else:
                    filtros.Element('incVAL1').update(value='')    
            
            elif(values['VAL1']=='' and values['VAL2']!='Dados Incoerentes'):
                
                aval[0]=1
                filtros.Element('incVAL1').update(value='Valor inválido')
                filtros.Element('incVAL2').update(value='')
                filtros.Element('incLOG').update(value='')
                
                try:
                    if(float(values['VAL2'])<0):
                        filtros.Element('incVAL2').update(value='Valor inválido')
                except:
                    filtros.Element('incVAL2').update(value='Valor inválido')
                else:
                    filtros.Element('incVAL2').update(value='') 
                    aval[0]=0
            try:        
                if(float(values['VAL1'])<float(values['VAL2'])):
                    aval[0]=1
                    filtros.Element('incLOG').update(value='Dados Incoerentes')
            except:
                try:
                    float(values['VAL1'])
                except:
                    filtros.Element('incVAL1').update(value='Valor inválido')
                
                try:
                    float(values['VAL2'])
                except:
                    filtros.Element('incVAL2').update(value='Valor inválido')
            else:
                aval[0]=0
                filtros.Element('incVAL1').update(value='')
                filtros.Element('incVAL2').update(value='')
                filtros.Element('incLOG').update(value='')            
                           
            if(values['inicioDATA']=='' and values['fimDATA']==''):
                filtros.Element('incDATA1').update(value='')
                filtros.Element('incDATA2').update(value='')
                filtros.Element('incLOG').update(value='')
                aval[1]=0
                
            if(aval==[0,0]):
                filtros.close()
                return values                
               
        if event == 'Cancelar':
            filtros.close()
            return default 
                        
        if event==sg.WIN_CLOSED:            
            filtros.close()
            return default 
        
    filtros.close()
