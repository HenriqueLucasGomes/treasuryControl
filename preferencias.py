from os import dup2
import PySimpleGUI as sg
import arq_control

def prefer (user,meio,default):
    sg.theme('DarkAmber')   
    
    data='1'
    valor='2'
    nom='3'
    
    saida=True
    d1=('black','yellow')
    d2=('black','yellow')
    d3=('black','yellow')
    v1=('black','yellow')
    v2=('black','yellow')
    v3=('black','yellow')
    n1=('black','yellow')
    n2=('black','yellow')
    n3=('black','yellow')
    dc=False
    dd=False
    vc=False
    vd=False
    nc=False
    nd=False
        
    if(default['data']=='1'):
        d2=('black','gray')
        d3=('black','gray')
        data='1'
    elif(default['data']=='2'):
        d1=('black','gray')
        d3=('black','gray')
        data='2'
    elif(default['data']=='3'):
        d2=('black','gray')
        d1=('black','gray')
        data='3'
        
    if(default['valor']=='1'):
        v2=('black','gray')
        v3=('black','gray')
        valor='1'
    elif(default['valor']=='2'):
        v1=('black','gray')
        v3=('black','gray')
        valor='2'
    elif(default['valor']=='3'):
        v2=('black','gray')
        v1=('black','gray')
        valor='3'
        
    if(default['nome']=='1'):
        n2=('black','gray')
        n3=('black','gray')
        nom='1'
    elif(default['nome']=='2'):
        n1=('black','gray')
        n3=('black','gray')
        nom='2'
    elif(default['nome']=='3'):
        n2=('black','gray')
        n1=('black','gray')
        nom='3'
        
    if(default['dataT']=='C'):
        dc=True
        dd=False
    else:
        dc=False
        dd=True
    
    if(default['valorT']=='D'):
        vc=False
        vd=True
    else:
        vc=True
        vd=False

    
    if(default['nomeT']=='D'):
        nc=False
        nd=True
    else:
        nc=True
        nd=False


    if(meio=='saida'):
        saida=False
    elif(meio=='entrada'):
        saida=True

    layout = [ 
                [sg.Text('Preferências',font=('Times Roman',30),pad=(0,(20,20)))],              
                
                [sg.Text('Data:',pad=((5,22),(0,0)),font=('Times Roman',20)), sg.Button('1°', key="D1", font=('Times Roman',12),button_color=d1),
                 sg.Button('2°', key="D2", font=('Times Roman',12),button_color=d2),sg.Button('3°', key="D3", font=('Times Roman',12),button_color=d3,visible=saida),
                 sg.Radio('Crescente','data',default=dc),sg.Radio('Descrescente','data',default=dd)],        
                
                [sg.Text('Valor:',pad=((8,13),(0,0)),font=('Times Roman',20)), sg.Button('1°', key="V1", font=('Times Roman',12),button_color=v1), 
                 sg.Button('2°', key="V2", font=('Times Roman',12),button_color=v2),sg.Button('3°', key="V3", font=('Times Roman',12),button_color=v3,visible=saida),
                 sg.Radio('Crescente','valor',default=vc),sg.Radio('Descrescente','valor',default=vd)],        
                
                [sg.Text('Nome:',pad=((5,22),(0,0)),font=('Times Roman',20),visible=saida), sg.Button('1°', key="N1", font=('Times Roman',12),button_color=n1,visible=saida),        
                 sg.Button('2°', key="N2", font=('Times Roman',12),button_color=n2,visible=saida),sg.Button('3°', key="N3", font=('Times Roman',12),button_color=n3,visible=saida),
                 sg.Radio('Crescente','nome',visible=saida,default=nc),sg.Radio('Descrescente','nome',visible=saida,default=nd)],
            
                # [sg.Listbox(tipos, pad=(0,(40,0)), default_values = default['tipos'], key='tipos',size=(15,1), font=('Times Roman',15))],
                
                [sg.Button('Alterar',pad=(30,50),font=('Times Roman',15)), sg.Button('Cancelar',pad=(20,50),font=('Times Roman',15))]
                
            ]


    prefer = sg.Window(
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
        
        event, values = prefer.read()
            
        if event == 'D1':
            prefer.Element('D1').update(button_color=('black','yellow'))
            prefer.Element('D2').update(button_color=('black','gray'))
            prefer.Element('D3').update(button_color=('black','gray'))
            data='1'
        if event == 'D2':
            prefer.Element('D2').update(button_color=('black','yellow'))
            prefer.Element('D1').update(button_color=('black','gray'))
            prefer.Element('D3').update(button_color=('black','gray'))
            data='2'
        if event == 'D3':
            prefer.Element('D3').update(button_color=('black','yellow'))
            prefer.Element('D1').update(button_color=('black','gray'))
            prefer.Element('D2').update(button_color=('black','gray'))
            data='3'
        
        if event == 'V1':
            prefer.Element('V1').update(button_color=('black','yellow'))
            prefer.Element('V2').update(button_color=('black','gray'))
            prefer.Element('V3').update(button_color=('black','gray'))
            valor='1'
        if event == 'V2':
            prefer.Element('V2').update(button_color=('black','yellow'))
            prefer.Element('V1').update(button_color=('black','gray'))
            prefer.Element('V3').update(button_color=('black','gray'))
            valor='2'
        if event == 'V3':
            prefer.Element('V3').update(button_color=('black','yellow'))
            prefer.Element('V1').update(button_color=('black','gray'))
            prefer.Element('V2').update(button_color=('black','gray'))
            valor='3'
            
        if event == 'N1':
            prefer.Element('N1').update(button_color=('black','yellow'))
            prefer.Element('N2').update(button_color=('black','gray'))
            prefer.Element('N3').update(button_color=('black','gray'))
            nom='1'
        if event == 'N2':
            prefer.Element('N2').update(button_color=('black','yellow'))
            prefer.Element('N1').update(button_color=('black','gray'))
            prefer.Element('N3').update(button_color=('black','gray'))
            nom='2'
        if event == 'N3': 
            prefer.Element('N3').update(button_color=('black','yellow'))
            prefer.Element('N1').update(button_color=('black','gray'))
            prefer.Element('N2').update(button_color=('black','gray'))
            nom='3'
        
        
        if event == 'Alterar': 
            
            print(values)
            
            if(values[0]==True):
                d='C' 
            else:
                d='D'
            if(values[2]==True):
                v='C'
            else:
                v='D'
            if(values[4]==True):
                n='C'
            else:
                n='D'
             
            prefer.close()     
            return {'data':data,'dataT':d,'valor':valor,'valorT':v,'nome':nom,'nomeT':n}
                        
               
        if event == 'Cancelar':
            prefer.close()
            return default 
                        
        if event==sg.WIN_CLOSED:            
            prefer.close()
            return default 
        
    prefer.close()
