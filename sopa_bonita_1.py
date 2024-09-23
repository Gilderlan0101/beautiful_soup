import requests
from bs4 import BeautifulSoup

def info_do_site():
    headers = {'User-Agent': 'Mozilla/5.0'}  # Emula um navegador
    url = "https://www.w3schools.com/python/python_json.asp"
    resposta = requests.get(url, headers=headers)
    print(resposta)

    if resposta.status_code == 200:  # Requisição OK
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # importando todas as div expecifica
        titulos = soup.find_all('div', class_='w3-example')

        # Itera sobre cada título encontrado e exibe o texto
        for h in titulos:
            print(h.text.strip())  # Imprime o conteúdo de cada h3

go_in_site = info_do_site()
