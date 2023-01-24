from datetime import datetime
import requests


def ret_detalhes_fechamento(pjson: list) -> str:
    valor = pjson[0]['name']
    for i in pjson:
        valor += f"\n- Compra: {i['bid']} \n" \
                 f"- Venda: {i['ask']} \n" \
                 f"- Variação: {i['varBid']} \n" \
                 f"- Porcentagem de Variação: {i['pctChange']} \n" \
                 f"- Máximo: {i['high']} \n" \
                 f"- Mínimo: {i['low']} \n" \
                 f"- Data: {datetime.fromtimestamp(int(i['timestamp'])).strftime('%d/%m/%Y %H:%M:%S')}\n"
    return valor


def ret_detalhes_cotacao(chave_pai: str, pjson: dict) -> str:
    return f"\n{pjson[chave_pai]['name']} \n" \
           f"- Compra: {pjson[chave_pai]['bid']} \n" \
           f"- Venda: {pjson[chave_pai]['ask']} \n" \
           f"- Variação: {pjson[chave_pai]['varBid']} \n" \
           f"- Porcentagem de Variação: {pjson[chave_pai]['pctChange']} \n" \
           f"- Máximo: {pjson[chave_pai]['high']} \n" \
           f"- Mínimo: {pjson[chave_pai]['low']} \n" \
           f"- Dados gerados em: {datetime.today().strftime('%d/%m/%Y %H:%M:%S')}"


def ret_texto_default(busca_por: str):
    response = None
    if busca_por == 'combinacoes':
        response = requests.get('https://economia.awesomeapi.com.br/xml/available').content
    elif busca_por == 'moedas':
        response = requests.get('https://economia.awesomeapi.com.br/xml/available/uniq').content

    return response


def seta_tema_padrao(tema: str) -> None:
    with open('TemaDefault/tema.txt', 'w') as tema_padrao:
        tema_padrao.write(tema)


def ret_tema_padrao() -> str:
    with open('TemaDefault/tema.txt', 'r') as tema_padrao:
        tema = tema_padrao.read()
        if tema:
            return tema
        else:
            return 'DarkGray2'
