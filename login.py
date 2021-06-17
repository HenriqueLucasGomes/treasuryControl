import PySimpleGUI as sg
import img 
import cadastro
import arq_control
import tela_principal
import logging

def Login ():
    sg.theme('DarkAmber')   # Add a touch of color

    layout = [ 
                [sg.Text('Bem Vindo ao Assintente de Tesouraria!',font=('Times Roman',30),pad=(0,(50,0)))],
                [sg.Text('Por favor realize seu Login ou Cadastro.',font=('Times Roman',30), pad=(0,(0,50)))],
                [sg.Text('Usuário Incorreto', key="incUSER", visible=True, size=(20,1),  text_color='red',font=('Times Roman',11))],
                [sg.Text('Login:', key="logins", pad=(5,(0,0)),font=('Times Roman',20)), sg.InputText(key="usuario", size=(35,1),pad=(5,(0,0)),font=('Times Roman',12))],
                [sg.Text('Senha Incorreta', key="incSENHA", visible=True, size=(20,1), pad=(0,(10,0)), text_color='red',font=('Times Roman',11))],
                [sg.Text('Senha:',font=('Times Roman',20)), sg.InputText(key="senha",size=(35,1),password_char="*",font=('Times Roman',12))],
                [sg.Button('Entrar', pad=(30,50),font=('Times Roman',15)), sg.Button('Cadastrar-se',pad=(20,50),font=('Times Roman',15))],
                [sg.Image(data=img.img_1,pad=((0,0),(60,0)))]
            ]


    login = sg.Window(
                    'Treasury Assistant', layout, size=(800,600), resizable=True,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    
    login.Element('incUSER').update(visible=False)
    login.Element('incSENHA').update(visible=False)

    while True:
        event, values = login.read()
        if event == 'Entrar': 
            # print("Entrar "+values['usuario']+" "+values['senha'])
            logging.info("[>] Login: "+values['usuario']+' '+values['senha'])
            
            if arq_control.consultUser(values['usuario'])==False:
                login.Element('incUSER').update(visible=True)
                logging.warning('[>] Usuário incorreto')
            elif arq_control.consultSenha(values['usuario'],values['senha'])==False:
                login.Element('incUSER').update(visible=False)
                login.Element('incSENHA').update(visible=True)
                logging.warning('[>] Senha incorreta')
            else:
                login.Element('incUSER').update(visible=False)
                login.Element('incSENHA').update(visible=False)
                logging.info("[>] Login Realizado!")
                login.close()
                tela_principal.tela_principal(arq_control.getIsntanc(values['usuario']))
                
                
        if event == 'Cadastrar-se':
            logging.info("[>] Cadastro Selecionado")
            login.Element('incUSER').update(visible=False)
            login.Element('incSENHA').update(visible=False)
            login.hide()
            cadastro.cadrastrar(login)
        if event==sg.WIN_CLOSED:
            logging.info('[>] Tela Fechada')
            break
        
    login.close()
