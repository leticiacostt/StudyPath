from json_manager import carregar_dados, salvar_dados
from tabulate import tabulate
from datetime import datetime

# Adiciona um novo arquivo JSON
def adicionar_estudo():

    while True:
        materia_estudada = input("Qual matéria você estudou hoje? ").strip().title()

        if materia_estudada == "":
            print("A matéria não pode ficar vazia!")
        else:
            break

    while True:
        assunto_estudado = input("Informe o assunto estudado: ").strip().title()

        if assunto_estudado == "":
            print("O assunto não pode ficar vazio!")
        else:
            break

    while True:    
        data_estudada = input("Informe a data (DD/MM/AAAA): ").strip()

        if data_estudada == "":
            print("A data não pode ficar vazia!")
            continue

        try:
            datetime.strptime(data_estudada, "%d/%m/%Y")
            break
        except ValueError:
            print("Informe uma data válida no formato DD/MM/AAAA!")

    while True:
        try:
            horas_estudadas = float(input("Informe as horas estudadas: "))

            if horas_estudadas <= 0:
                print("As horas devem ser maior do que zero!")
            else:
                break

        except ValueError:
            print("Informe um número válido!")

    # Cria um dicionário com as informações do novo estudo
    novo_estudo = {
        "materia": materia_estudada,
        "assunto": assunto_estudado,
        "data": data_estudada,
        "horas": horas_estudadas
    }

    dados = carregar_dados()

    # Define o ID ndo novo estudo
    if dados["estudos"]:
        proximo_id = max(estudo["id"] for estudo in dados ["estudos"]) + 1
    else:
        proximo_id = 1

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
            estudo["materia"],
            estudo["assunto"],
            estudo["data"], 
            estudo["horas"]
        ])

    print("\n========== MATÉRIAS ESTUDADAS ==========\n")

    # Exibe os estudos em formato de tabela
    print(tabulate(
        tabela, 
        headers = ["ID", "Matéria", "Assunto", "Data", "Horas"],
        tablefmt="grid"
    ))

# Edita um estudo
def editar_estudo():
    while True:
        try:
            id_editar = int(input("Qual o ID do estudo que deseja editar? "))
            break
        except ValueError:
            print("Digite um ID válido!")

    dados = carregar_dados()

    for estudo in dados["estudos"]:
        if estudo["id"] == id_editar:
            print("Estudo encontrado!")

            while True:
                print("\n1 - Alterar matéria")
                print("2 - Alterar assunto")
                print("3 - Alterar data")
                print("4 - Alterar horas")
                print("5 - Finalizar edição")

                opcao = input("Escolha uma opção: ").strip()

                if opcao == "1":
                # Altera matéria
                    while True:
                        nova_materia = input("Digite a nova matéria: ").strip().title()

                        if nova_materia == "":
                            print("A matéria não pode ficar vazia!")
                        else:
                            estudo["materia"] = nova_materia
                            print("Matéria atualizada!")
                            break

                elif opcao == "2":
                    # Altera o assunto
                    while True:
                        novo_assunto = input("Digite o novo assunto: ").strip().title()

                        if novo_assunto == "":
                            print("O assunto não pode ficar vazio!")
                        else:
                            estudo["assunto"] = novo_assunto
                            print("Assunto atualizado!")
                            break

                elif opcao == "3":
                    # Altera a data
                    while True:
                        nova_data = input("Digite a nova data (DD/MM/AAAA): ")

                        if nova_data == "":
                            print("A data não pode ficar vazia!")
                            continue

                        try:
                            datetime.strptime(nova_data, "%d/%m/%Y")
                            estudo["data"] = nova_data
                            print("Data atualizada!")
                            break
                        except ValueError:
                            print("Informe uma data válida no formato DD/MM/AAAA!")

                elif opcao == "4":
                    # Altera as horas
                    while True:
                        try:
                            novas_horas = float(input("Digite as novas horas: "))

                            if novas_horas <= 0:
                                print("As horas devem ser maiores do que zero!")
                            else:
                                estudo["horas"] = novas_horas
                                print("Horas atualizadas!")
                                break

                        except ValueError:
                            print("Informe um número válido!")

                elif opcao == "5":
                    salvar_dados(dados)
                    print("Edição finalizada!")
                    return

                else:
                    print ("opção inválida! Escolha uma opção de 1 a 5.")

    print("Estudo não encontrado!")

# Remove um estudo do arquivo JSON
def remover_estudos():
    while True:
        try:
            id_remover = int(input("Qual ID de estudo você deseja remover? "))
            break
        except ValueError:
            print("Digite um ID válido!")

    materias = carregar_dados()

    # Percorre os estudos procurando o registro informado pelo usuário
    for materia in materias["estudos"]:
        if materia["id"] == id_remover:
            materias["estudos"].remove(materia)

            # Reorganiza os estudos procurando o registro informado pelo usuário
            for indice, estudo in enumerate(materias["estudos"], start=1):
                estudo["id"] = indice

            salvar_dados(materias)
            print("Matéria Removida!")
            return
        
    print("Estudo não encontrado!")