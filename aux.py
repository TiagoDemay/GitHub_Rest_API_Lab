import requests
import os

# Variavel de ambiente para o Token do GitHub
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
token = GITHUB_TOKEN

class repos_wiki():

    def __init__(self, urls):
        self._urls = urls

    def requisicao_api(self):
        resposta = requests.get(f'https://github.com/Insper/{self._urls}/wiki', auth=('your_user',token))
        if resposta.status_code == 200:
            return resposta.url
        else:
            return resposta.status_code
