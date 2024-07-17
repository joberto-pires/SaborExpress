import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_res = {}

    for item in dados_json:
        nome_res = item['Company']

        if nome_res not in dados_res:
            dados_res[nome_res] = []

        dados_res[nome_res].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'o erro foi {response.status_code}')
for nome_res, dados in dados_res.items():
    nome_arquivo = f'{nome_res}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent = 4)
