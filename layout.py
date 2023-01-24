from PySimpleGUI import PySimpleGUI as Sg
from utils import ret_texto_default


def define_tema(tema: str) -> None:
    Sg.theme(tema)


def layout_help() -> list:
    return [
        [
            Sg.Text('Lista completa de combinações')
        ],
        [
            Sg.Multiline(default_text=ret_texto_default('combinacoes'),
                         key='help_combinacoes',
                         size=(60, 7),
                         no_scrollbar=False,
                         disabled=True)
        ],
        [
            Sg.Text('Lista de nomes das moedas')
        ],
        [
            Sg.Multiline(default_text=ret_texto_default('moedas'),
                         key='help_moedas',
                         size=(60, 6),
                         no_scrollbar=False,
                         disabled=True)
        ]
    ]


def layout_principal() -> list:
    return [
        [
            Sg.Text('Conversão de valores'),
            Sg.Text(' ' * 65),
            Sg.Button(image_filename='Imagens/interrogacao.png', key='help')
        ],
        [
            Sg.Text('De:'), Sg.Input(key='kde', size=(20, 1)),
            Sg.Text('Para:'), Sg.Input(key='kpara', size=(20, 1)),
            Sg.Button('Buscar', key='buscar_convercao')
        ],
        [
            Sg.Multiline(key='textbox', size=(60, 5), no_scrollbar=False, disabled=True)
        ],
        [
            Sg.Text('Fechamento dos ultimos'), Sg.Input(key='dias', size=(3, 1)),
            Sg.Text('Dias'),
            Sg.Button('Buscar', key='buscar_fechamento')
        ],
        [
            Sg.Multiline(key='textbox_fechamento', size=(60, 5), no_scrollbar=False, disabled=True)
        ],
        [
            [Sg.Text('Temas disponíveis')],
            [
                Sg.Listbox(values=Sg.theme_list(),
                           size=(20, 5),
                           key='temas',
                           enable_events=True),
                Sg.Button('Setar como Padrão', key='tema_padrao'),
                Sg.Text(' ' * 6),
                Sg.Button('Limpar/Redefinir', key='limpar')
            ]
        ]
    ]


def window(playout: str) -> Sg.Window:
    layout = None
    if playout == 'principal':
        layout = layout_principal()
    elif playout == 'help':
        layout = layout_help()

    return Sg.Window('Economia', layout, size=(465, 360), icon='Imagens/Ico_Princ.ico')
