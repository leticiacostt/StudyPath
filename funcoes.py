#Regras e funcionalidades do StudyPath, como adicionar, editar, remover e visualizar estudos
from tabulate import tabulate
from datetime import datetime
from banco import (
    buscar_estudos,
    buscar_materia,
    inserir_estudo,
    editar_estudo_banco,
    remover_estudo
)

# Adiciona um novo arquivo JSON
def adicionar_estudo():

    while True:
        materia_estudada = input("Qual matéria você estudou hoje? ").strip()

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

    materia = buscar_materia(materia_estudada)

    if materia is None:
        print("Matéria não cadastrada!")
        return

    materia_id = materia[0]

    inserir_estudo(
        materia_id,
        assunto_estudado,
        data_estudada,
        horas_estudadas
    )

    print("Estudo adicionado!")

# Exibe todos os estudos cadastrados
def ver_estudos():
    resultados = buscar_estudos()

    # Cria uma lista para armazenar os estudos
    tabela = []

    for numero, estudo in enumerate(resultados, start=1):
        tabela.append([
            numero,
            estudo[0],
            estudo[1],
            estudo[2],
            estudo[3],
            estudo[4]
        ])

    print("\n========== MATÉRIAS ESTUDADAS ==========\n")

    # Exibe os estudos em formato de tabela
    print(tabulate(
        tabela,
        headers=["Nº", "ID", "Matéria", "Assunto", "Data", "Horas"],
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

    estudos = buscar_estudos()

    estudo_encontrado = None

    for estudo in estudos:
        if estudo[0] == id_editar:
            estudo_encontrado = estudo
            break

    if estudo_encontrado is None:
        print("Estudo não encontrado!")
        return

    print("Estudo encontrado!")

    materia_id = buscar_materia(estudo_encontrado[1])[0]
    assunto = estudo_encontrado[2]
    data = estudo_encontrado[3]
    horas = estudo_encontrado[4]

    while True:
        print("\n1 - Alterar matéria")
        print("2 - Alterar assunto")
        print("3 - Alterar data")
        print("4 - Alterar horas")
        print("5 - Finalizar edição")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            while True:
                nova_materia = input("Digite a nova matéria: ").strip()

                if nova_materia == "":
                    print("A matéria não pode ficar vazia!")
                else:
                    materia = buscar_materia(nova_materia)

                    if materia is None:
                        print("Matéria não cadastrada!")
                    else:
                        materia_id = materia[0]
                        print("Matéria atualizada!")
                        break

        elif opcao == "2":
            while True:
                novo_assunto = input("Digite o novo assunto: ").strip().title()

                if novo_assunto == "":
                    print("O assunto não pode ficar vazio!")
                else:
                    assunto = novo_assunto
                    print("Assunto atualizado!")
                    break

        elif opcao == "3":
            while True:
                nova_data = input("Digite a nova data (DD/MM/AAAA): ").strip()

                if nova_data == "":
                    print("A data não pode ficar vazia!")
                    continue

                try:
                    datetime.strptime(nova_data, "%d/%m/%Y")
                    data = nova_data
                    print("Data atualizada!")
                    break
                except ValueError:
                    print("Informe uma data válida no formato DD/MM/AAAA!")

        elif opcao == "4":
            while True:
                try:
                    novas_horas = float(input("Digite as novas horas: "))

                    if novas_horas <= 0:
                        print("As horas devem ser maiores do que zero!")
                    else:
                        horas = novas_horas
                        print("Horas atualizadas!")
                        break

                except ValueError:
                    print("Informe um número válido!")

        elif opcao == "5":
            editar_estudo_banco(
                id_editar,
                materia_id,
                assunto,
                data,
                horas
            )

            print("Edição finalizada!")
            return

        else:
            print("Opção inválida! Escolha uma opção de 1 a 5.")

# Remove um estudo do arquivo JSON
def remover_estudos():
    while True:
        try:
            id_remover = int(input("Qual ID de estudo você deseja remover? "))
            break
        except ValueError:
            print("Digite um ID válido!")

    estudos = buscar_estudos()

    estudo_encontrado = False

    for estudo in estudos:
        if estudo[0] == id_remover:
            estudo_encontrado = True
            break

    if not estudo_encontrado:
        print("Estudo não encontrado!")
        return

    remover_estudo(id_remover)

    print("Estudo removido!")