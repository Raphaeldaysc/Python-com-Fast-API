from fastapi import FastAPI, Query
import requests as re

app = FastAPI()


@app.get('/api/hello')
def hello_world():
    return {'hello': 'world'}


@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = re.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurantes = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurantes.append({
                    'item': item['Item'],
                    'preco': item['price'],
                    'descricao': item['description']
                })
        return {'Restaurante': restaurante, 'cardapio': dados_restaurantes}
    else:
        return {'error': f'{response.status_code} - {response.text}'}
