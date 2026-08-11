from json_manager import carregar_dados, salvar_dados
from tabulate import tabulate

# Adiciona um novo arquivo JSON
def adicionar_estudo():
    dia_estudado = input("Em qual dia da semana você estudou? ").strip()
    horas_estudadas = input("Quantas horas você estudou? ").strip()
    materia_estudada = input("Qual matéria você estudou hoje? ").strip()
    assunto_estudado = input("Qual o assunto estudado? ").strip()

    # Cria um dicionário com as informações do novo estudo
    novo_estudo = {
        "dia": dia_estudado,
        "horas": horas_estudadas,
        "materia": materia_estudada,
        "assunto": assunto_estudado
    }

    dados = carregar_dados()

    # Define o ID ndo novo estudo
    proximo_id = (len(dados["estudos"])) + 1

    #Adiciona o ID ao novo estudo
    novo_estudo["id"] = proximo_id

    # Adiciona o novo estudo à lista de estudos
    dados["estudos"].append(novo_estudo)

    salvar_dados(dados)
    
    print("Matéria adicionada!")

# Exibe todos os estudos cadastrados
def ver_estudos():
    conteudo = carregar_dados()

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

    dados = carregar_dados()

    for estudo in dados["estudos"]:
        if estudo["id"] == id_editar:
            print("Estudo encontrado!")

            nova_materia = input("Digite a nova matéria: ")
            estudo["materia"] = nova_materia

            break

    salvar_dados(dados)

# Remove um estudo do arquivo JSON
def remover_estudos():
    id_remover = int(input("Qual ID de estudo você deseja remover? "))

    materias = carregar_dados()

    # Percorre os estudos procurando o registro informado pelo usuário
    for materia in materias["estudos"]:
        if materia["id"] == id_remover:
            materias["estudos"].remove(materia)
            salvar_dados(materias)
            print("Matéria Removida!")
            return
        
    print("Estudo não encontrado!")