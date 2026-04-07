import time
import os

agenda = []
TEMPO = 3

while True:
    os.system("cls")

    print("------ AGENDA ------")
    print("1. Adicionar")
    print("2. Ver Contatos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("cls")

        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")

        contato = {
            "nome": nome,
            "telefone": telefone
        }

        agenda.append(contato)

        print(f"{contato["nome"]} foi adicionado com sucesso!")
        time.sleep(TEMPO)
        
    elif opcao == "2":
        os.system("cls")

        if len(agenda) == 0:
            print("A lista de contatos está vazia!")
            time.sleep(TEMPO)
            continue
        
        print("------ LISTA DE CONTATOS ------")

        for contato in agenda:
            print(f"| Nome: {contato['nome']} --- Telefone: {contato['telefone']} |")
        
        print("------ FIM DA LISTA DE CONTATOS ------")
        time.sleep(10)

    elif opcao == "3":
        os.system("cls")
        print("Finalizando aplicação...")
        time.sleep(TEMPO)
        break
    else:
        os.system("cls")
        print("Opção inválida, tente novamente!")
        time.sleep(TEMPO)