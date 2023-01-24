import requests
from PySimpleGUI import PySimpleGUI as Sg
from layout import window, define_tema
from utils import ret_detalhes_cotacao, ret_detalhes_fechamento, seta_tema_padrao, ret_tema_padrao

define_tema(ret_tema_padrao())
novo_tema = ''

janela = window('principal')

Sg.cprint_set_output_destination(janela, "resultado")

while True:
    eventos, valores = janela.read()

    if eventos == Sg.WIN_CLOSED:
        break

    if eventos == 'temas':
        define_tema(valores['temas'][0])
        novo_tema = valores['temas'][0]
        janela = window('principal')
        Sg.cprint_set_output_destination(janela, "resultado")

    if eventos == 'limpar':
        define_tema(ret_tema_padrao())
        janela = window('principal')
        Sg.cprint_set_output_destination(janela, "resultado")

    if eventos == 'tema_padrao':
        if novo_tema:
            seta_tema_padrao(novo_tema)

    if eventos == 'buscar_convercao':
        if valores['kde'] != '' and valores['kpara'] != '':
            r = requests.get(f"https://economia.awesomeapi.com.br/last/{valores['kde']}-{valores['kpara']}")

            Sg.cprint_set_output_destination(janela, 'textbox')
            Sg.cprint(ret_detalhes_cotacao(f"{valores['kde']}{valores['kpara']}".upper(), r.json()), key='textbox')
        else:
            Sg.popup_quick_message("Informe a moeda. Ex: USD-BRL,EUR-BRL,BTC-BRL")

    if eventos == 'buscar_fechamento':
        if valores['dias'] != '' and valores['kde'] != '' and valores['kpara'] != '':
            r = requests.get(f"https://economia.awesomeapi.com.br/json/daily/"
                             f"{valores['kde']}-{valores['kpara']}/{valores['dias']}")
            Sg.cprint_set_output_destination(janela, 'textbox_fechamento')
            Sg.cprint(ret_detalhes_fechamento(r.json()), key='textbox_fechamento')

    if eventos == 'help':
        janela_help = window('help')
        janela_help.read()
        define_tema("DarkGray")
