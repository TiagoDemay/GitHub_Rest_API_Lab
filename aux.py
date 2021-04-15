import requests
import os

# Variavel de ambiente para o Token do GitHub
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
token = GITHUB_TOKEN

class repos_wiki():

    def __init__(self, org="Insper"):
        self._org = org
   
    def requisicao_api_repos(self, page=1):
        self._page = page         
        response = requests.get(
            f"https://api.github.com/orgs/{self._org}/repos?per_page=100&page={self._page}", auth=('your_user',token))
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def requisicao_api_urls(self, urls):
        self._urls = urls
        resposta = requests.get(f'https://github.com/Insper/{self._urls}/wiki', auth=('your_user',token))
        if resposta.status_code == 200:
            return resposta.url
        else:
            return resposta.status_code
