#coordena tudo e mostra o menu para o usuário, chamando as funções do funcoes.py
from funcoes import adicionar_estudo, ver_estudos, editar_estudo, remover_estudos

print("========== DIÁRIO DE ESTUDOS ===========")

# Exibe o menu e controla as opções do usuário
while True:
    print("\n1- Adicionar matéria")
    print("2- Ver matérias")
    print("3- Editar matéria")
    print("4- Remover matéria")
    print("6- Sair")

    opcao = input("Escolha uma opção: ")

    # Adiciona um novo estudo
    if opcao == "1":
        adicionar_estudo()

    # Exibe os estudos cadastrados
    elif opcao == "2":
        ver_estudos()

    # Edita um estudo
    elif opcao == "3":
        editar_estudo()

    # Remove um estudo 
    elif opcao == "4":
        remover_estudos()

    # Encerra o programa
    elif opcao == "5":
        print("Encerrando o Diário de Estudos...")
        break

    else:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")