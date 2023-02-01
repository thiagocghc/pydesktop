import requests
import json

###SITES PARA BUSCA
#https://developers.receitaws.com.br/#/operations/queryCNPJFree
#https://www.sintegraws.com.br/api/documentacao-api-receita-federal.php

def consulta_cpf(cpf,data_nasc):
    url = "https://www.sintegraws.com.br/api/v1/execute-api.php"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cpf":"00000000000","data-nascimento":"00000000","plugin":"CPF"}

    response = requests.request("GET", url, params=querystring)

    dados = json.loads(response.text)

    print(response.text)


def consulta_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"00000000000000","plugin":"RF"}

    response = requests.request("GET", url, params=querystring)

    dados = json.loads(response.text)

    print(f"{dados['nome']},{dados['cnpj']}, {dados['telefone']},{dados['uf']} , {dados['logradouro']} ")

consulta_cnpj('00776574000660')


