import json

def carregar_dados():
    with open("estudos.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open("estudos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)