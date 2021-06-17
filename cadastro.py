import PySimpleGUI as sg
from config import *
import arq_control
import logging

def cadrastrar (log):
    sg.theme('DarkAmber')   

    layout = [ 
                [sg.Text('Usuário Já Existe', key="exsUSER", visible=True, size=(21,1), pad=(5,(30,0)), text_color='red',font=(fonte,11))],
                [sg.Text('Login:',pad=(5,(0,0)),font=(fonte,20)), sg.InputText(key="usuario", size=(35,4),pad=(5,(0,0)),font=(fonte,12))],
                [sg.Text('Senha:',font=(fonte,20)), sg.InputText(key="senha",size=(35,4),password_char="*",font=(fonte,12))],
                [sg.Text('Senhas Incompatíveis', key="icpSENHA", visible=True, size=(27,1),  justification='r', text_color='red',font=(fonte,11))],
                [sg.Text('Repetir:',font=(fonte,20)), sg.InputText(key="rep_senha",size=(31,4),password_char="*",font=(fonte,12))],
                [sg.Button('Cadastrar',pad=(30,50),font=(fonte,15)), sg.Button('Cancelar',pad=(20,50),font=(fonte,15))]
                
            ]


    cadastro = sg.Window(
                    'Treasury Assistant', layout,
                    element_justification="c", auto_close = False,
                    auto_close_duration=2, finalize=True,
                    icon='/home/henrique/Documentos/Tesouraria/sarca.png'
                ) #resizable=True, margins=(0,90),

    # window.maximize()
    
    cadastro.Element('exsUSER').update(visible=False)
    cadastro.Element('icpSENHA').update(visible=False)

    while True:
        event, values = cadastro.read()
            
        if event == 'Cadastrar':
            # print("Cadastrado: "+values['usuario']+' '+values['senha']+' '+values['rep_senha'])
            logging.info("[>] Cadastro: "+values['usuario']+' '+values['senha']+' '+values['rep_senha'])
            
            if arq_control.consultUser(values['usuario'])==True:
                logging.warning('[>] Usuário Existente')
                cadastro.Element('icpSENHA').update(visible=False)
                cadastro.Element('exsUSER').update(value='Usuário Já Existe',visible=True)
            elif values['usuario']=='':
                logging.warning('[>] Usuário Inválido')
                cadastro.Element('exsUSER').update(value="Usuário Inválido",visible=True)
                cadastro.Element('icpSENHA').update(visible=False)
            elif values['senha']!=values['rep_senha']:
                logging.warning('[>] Senhas diferentes')
                cadastro.Element('exsUSER').update(visible=False)
                cadastro.Element('icpSENHA').update(value='Senhas Incompatíveis',visible=True)
            elif values['senha']=='':
                logging.warning('[>] Senha Inválida')
                cadastro.Element('exsUSER').update(visible=False)
                cadastro.Element('icpSENHA').update(value="Senha Inválida",visible=True)
            else:
                logging.info("[>] Cadastrado Aceito")
                cadastro.Element('exsUSER').update(visible=False)
                cadastro.Element('icpSENHA').update(visible=False)
                if arq_control.criarUser(values['usuario'],values['senha'])==True:
                    sg.Popup("Novo Usuário Cadastrado!!!")
                    logging.info("[>] Usuário Cadastrado")
                    cadastro.close()
                    log.un_hide()
                    break
                else:
                    logging.error("[>] Erro ao Cadastrar")
                    sg.Popup("Erro ao Cadastrar :(")
                    cadastro.close()
                    log.un_hide()
                    break
                
        if event == 'Cancelar':
            logging.info('[>] Evento Cancelado')
            # cadastro.hide()
            cadastro.close()
            log.un_hide()
            break
        if event==sg.WIN_CLOSED:
            logging.info('[>] Tela Fechada')
            log.un_hide()
            break
        
    cadastro.close()
