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



r1 = requests.get(
    f"https://api.github.com/orgs/Insper/repos?per_page=100&page=1", auth=('your_user',token))
resp1 = r1.json() 

r2 = requests.get(
    f"https://api.github.com/orgs/Insper/repos?per_page=100&page=2", auth=('your_user',token))
resp2 = r2.json()

if type(resp1) is not int:
    for i in range(len(resp1)):
        print('Index:', i, 'Repo:',resp1[i]['name'])
        urls = (resp1[i]['name'])
        u = repos_wiki(urls).requisicao_api()
        r = 'https://github.com/Insper/{}/wiki'.format(urls)
        if u == r:
            print('Wiki encontrada neste repositório')     
else:
    print("Erro... - Status Code:", resp1)

if type(resp2) is not int:
    for i in range(len(resp2)):
        print('Index:', i+100, 'Repo:',resp2[i]['name'])
        urls = (resp2[i]['name'])
        u = repos_wiki(urls).requisicao_api()
        r = 'https://github.com/Insper/{}/wiki'.format(urls)
        if u == r:
            print('Wiki encontrada neste repositório')  
else:
    print("Erro... - Status Code:", resp2)




# #   Modo de utilizar a biblioteca PyGithub
# user = g.get_user()
# print("O usuário que está fazendo a consulta é o:", user.login)

# print(user.get_repos().totalCount)
# for repo in user.get_repos():
#     print(repo.name)
#     print(repo.full_name)
#     print(repo.has_wiki)
