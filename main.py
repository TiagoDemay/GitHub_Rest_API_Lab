###   Projeto de consumo da API GITHUB via python    ###
### Laboratório de redes e Supercomputação da Insper ###

import requests
import json
import os

# A biblioteca PyGithub precisa ser instalada via pip 
# pip install PyGithub  

from github import Github
from aux import repos_wiki


# A Variavel $GITHUB_TOKEN deve ser criada no S.O com o valor do Token de acesso do Github pessoal
# Este comando busca a variavel no ambiente do usuário
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
token = GITHUB_TOKEN
# Autenticação e para utilizar a Biblioteca PyGithub 
g = Github(GITHUB_TOKEN)

organiz = 'Insper'

# Aqui usaremos dois objetos, pois a paginação do requests só suporta 100 itens.
r1 = repos_wiki(organiz).requisicao_api_repos(1)
r2 = repos_wiki(organiz).requisicao_api_repos(2)

if type(r1) is not int:
    for i in range(len(r1)):
        print('Index:', i, 'Repo:',r1[i]['name'])
        urls = (r1[i]['name'])
        u = repos_wiki().requisicao_api_urls(urls)
        r = 'https://github.com/Insper/{}/wiki'.format(urls)
        if u == r:
            print('Wiki encontrada neste repositório')     
else:
    print("Erro... - Status Code:", r1)

if type(r2) is not int:
    for i in range(len(r2)):
        print('Index:', i+100, 'Repo:',r2[i]['name'])
        urls = (r2[i]['name'])
        u = repos_wiki().requisicao_api_urls(urls)
        r = 'https://github.com/Insper/{}/wiki'.format(urls)
        if u == r:
            print('Wiki encontrada neste repositório')  
else:
    print("Erro... - Status Code:", r2)




# #   Modo de utilizar a biblioteca PyGithub
# user = g.get_user()
# print("O usuário que está fazendo a consulta é o:", user.login)

# print(user.get_repos().totalCount)
# for repo in user.get_repos():
#     print(repo.name)
#     print(repo.full_name)
#     print(repo.has_wiki)
