Exemplo Básico de Raspagem de Dados com Beautiful Soup em Python

Este é um exemplo básico de como pegar uma <div> ou qualquer outra tag HTML usando Beautiful Soup em Python.
Passo 1: Importar as Bibliotecas Necessárias

Primeiro, você importa as bibliotecas necessárias:

python

import requests
from bs4 import BeautifulSoup

    Requests: Biblioteca Python para requisição HTTP.
    BeautifulSoup: Biblioteca usada para raspar as informações dos sites.

Passo 2: Simular um Navegador

Alguns sites reconhecem que estamos tentando acessar o site com um script Python. Para evitar isso, vamos criar um header:

python

headers = {'User-Agent': 'Mozilla/5.0'}  # Emula um navegador

Passo 3: Fazer a Requisição

Vamos pegar o link do site que vamos fazer a raspagem. No meu caso:

python

url = "https://www.w3schools.com/python/python_json.asp"
resposta = requests.get(url, headers=headers)

Código Completo

python

def info_do_site():
    headers = {'User-Agent': 'Mozilla/5.0'}  # Emula um navegador
    url = "https://www.w3schools.com/python/python_json.asp"
    resposta = requests.get(url, headers=headers)
    print(resposta)

    if resposta.status_code == 200:  # Requisição OK
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # Importando a div específica
        titulos = soup.find_all('div', class_='w3-example')  # Aqui você irá colocar qual div você quer pegar, ou atributos ou tags

        # Itera sobre cada título encontrado e exibe o texto
        for h in titulos:
            print(h.text.strip())  # Imprime o conteúdo de cada div

go_in_site = info_do_site()

Saída Esperada

swift

<Response [200]>
Example
Import the json module:

    import json
Example
Convert from JSON to Python:

    import json
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    y = json.loads(x)  # the result is a Python dictionary:
    print(y["age"])
Try it Yourself »
...

Esse foi um exemplo básico de como fazer uma raspagem usando Beautiful Soup.
