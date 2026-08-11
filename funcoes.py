import json
from tabulate import tabulate

# Adiciona um novo arquivo JSON
def adicionar_estudo():
    dia_estudado = input("Em qual dia da semana você estudou? ")
    horas_estudadas = input("Quantas horas você estudou? ")
    materia_estudada = input("Qual matéria você estudou hoje? ")
    assunto_estudado = input("Qual o assunto estudado? ")

    # Cria um dicionário com as informações do novo estudo
    novo_estudo = {
        "dia": dia_estudado,
        "horas": horas_estudadas,
        "materia": materia_estudada,
        "assunto": assunto_estudado
    }

    # Abre o arquivo JSON para leitura
    with open("estudos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Define o ID ndo novo estudo
    proximo_id = (len(dados["estudos"])) + 1

    #Adiciona o ID ao novo estudo
    novo_estudo["id"] = proximo_id

    # Adiciona o novo estudo à lista de estudos
    dados["estudos"].append(novo_estudo)

    # Abre o arquivo JSON para escrita e salva os dados atualizados
    with open("estudos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    
        print("Matéria adicionada!")

# Exibe todos os estudos cadastrados
def ver_estudos():
    # Abre o arquivo JSON para leitura
    with open("estudos.json", "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)

    # Cria uma lista para armazenar os estudos
    tabela = []


    # Percorre cada estudo armazenado no JSON
    for estudo in conteudo["estudos"]:
        tabela.append([
            estudo["id"],
            estudo["dia"],
            estudo["horas"],
            estudo["materia"], 
            estudo["assunto"]
        ])

    print("\n========== MATÉRIAS ESTUDADAS ==========\n")

    # Exibe os estudos em formato de tabela
    print(tabulate(
        tabela, 
        headers = ["ID", "Dia", "Horas", "Matéria", "Assunto"],
        tablefmt="grid"
    ))

# Edita um estudo
def editar_estudo():
    id_editar = int(input("Qual o ID do estudo que deseja editar? "))

    # Abre o arquivo JSON para leitura
    with open("estudos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    for estudo in dados["estudos"]:
        if estudo["id"] == id_editar:
            print("Estudo encontrado!")

            nova_materia = input("Digite a nova matéria: ")
            estudo["materia"] = nova_materia

            break

    with open("estudos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Remove um estudo do arquivo JSON
def remover_estudos():
    dia_remover = input("Qual dia da semana você deseja remover? ")
    horas_remover = input("Qual carga horária você deseja remover? ")
    materia_remover = input("Qual matéria você deseja remover? ")
    assunto_remover = input("Qual assunto você deseja remover? ")

    # Abre o arquivo JSON para leitura
    with open("estudos.json", "r", encoding="utf=8") as arquivo:
        materias = json.load(arquivo)

    # Percorre os estudos procurando o registro informado pelo usuário
    for materia in materias["estudos"]:
        if(materia["dia"] == dia_remover and
            materia["horas"] == horas_remover and
            materia["materia"] == materia_remover and
            materia["assunto"] == assunto_remover):

            # Remove o estudo encontrado da lista
            materias["estudos"].remove(materia)

    # Salva o arquivo JSON com os dados atualizados
    with open("estudos.json", "w", encoding="utf=8") as arquivo:
        json.dump(materias, arquivo, indent=4, ensure_ascii=False)

    print("Matéria removida!")