# ConsultorMoedas
- App Pyhton, responsável por consultar a cotação de moedas disversas, consultando API docs.awesomeapi gratuita

#requirements
PySimpleGUI~=4.60.4
requests~=2.28.2

# consultor.py
- Responspavel por gerenciar os eventos dos Layouts Principal e Help 
- Eventos
  - temas -> listbox de todos os temas disponíveis no PySimpleGUI
  - limpar -> redefine o tema salvo no default e recarrega o form
  - tema_padrao -> seta novamente o tema padrão salvo na pasta TemaDefault
  - buscar_convercao -> consulta api que retorna a conversão "De/Para" com valores de "Compra, Venda, Variação, Porcentagem de Variação, Máximo, Mínimo e data da geração". EndPoint consultado: https://economia.awesomeapi.com.br/last/{:DE}-{:PARA}
  - buscar_fechamento -> Retorna o Fechamento dos ultimos X dias com valores de "Compra, Venda, Variação, Porcentagem de Variação, Máximo, Mínimo e data de fechamento". EndPoint consultado: https://economia.awesomeapi.com.br/json/daily/{:DE}-{:PARA}/{:XDIAS}
  - help -> Chama uma nova janela, com informativo de quais moedas estão disponiveis na Conversão e qual sigla usar para cada moeda
 
 #utils.py
 - ret_detalhes_fechamento -> Responsável por formatar o Json para apresentar dados do fechamento
 - ret_detalhes_cotacao -> Responsável por formatar o Json para apresentar dados da cotação
 - ret_texto_default -> Formata o Json das Conbinações e das Moedas da janela Help para apresentação dos dados
 - ret_tema_padrao -> Lê o arquivo "TemaDefault/tema.txt" para buscar o tema padrão, caso esteja vazio o arquivo, é setado o tema "DarkGray"
 - seta_tema_padrao -> Seta o Tema padrão no arquivo "TemaDefault/tema.txt"

#layout
- define_tema -> aplica o tema escolhido
- layout_help -> Monta tela de ajuda, com detalhes da conversão e do fechamento
- layout_principal -> Monta tela principal
- window -> carrega dados dos layouts

#setup
Este arquivo é responsável por gerar o .exe da aplicação
- build_exe_options -> Pacotes necessários para execução do exe com base na aplicação
- base -> seta se 32 ou 64 bits
- setup -> gera o executável com detalhes do produto
Para executar, basta acessar o terminal do pychar e digitar: "python .\setup.py build" ou pelo qualquer outro terminal estando dentro da pasta raiz do projeto

#Pastas
- DLLs -> Contem as DLLs necessárias para executar o .exe (python3.dll e python310.dll)
- Imagens -> Icone do form principal e do botão de Ajuda
- TemaDefault -> Contem o arquivo de texto responsável por armazenar o Tema Padrão
