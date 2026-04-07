import time
import os

agenda = []
# Variáveis em MAIÚSCULO são "Constantes" (valores que não mudam).
TEMPO = 3  

while True:
    # Limpa a tela antes de mostrar o menu
    os.system("cls") 

    print("------ AGENDA ------")
    print("1. Adicionar")
    print("2. Ver Contatos")
    print("3. Limpar Lista de Contatos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("cls")
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")

        contato_clonado = False

        for contato in agenda:
            if contato['nome'].strip().lower() == nome.strip().lower():
                contato_clonado = True
                break
        
        if contato_clonado:
            print(f"O contato {nome} já existe!")
            time.sleep(TEMPO)
        else:
            # Montamos a "ficha" (Dicionário) e guardamos na "prateleira" (Lista)
            contato = {
                "nome": nome,
                "telefone": telefone,
                "email": email
            }
            agenda.append(contato)

            # Atenção à aspa simples no ['nome'] para não dar SyntaxError!
            print(f"{contato['nome']} foi adicionado com sucesso!")
            time.sleep(TEMPO)
        
    elif opcao == "2":
        os.system("cls")

        # Se a prateleira estiver vazia, avisa e volta para o menu (continue)
        if len(agenda) == 0:
            print("A lista de contatos está vazia!")
            time.sleep(TEMPO)
            continue 
        
        print(f"Você tem {len(agenda)} contatos salvos.")
        print("------ LISTA DE CONTATOS ------")
        # O for percorre a lista e desempacota o dicionário
        for contato in agenda:
            print(f"| Nome: {contato['nome']} --- Telefone: {contato['telefone']} --- E-mail: {contato['email']} |")
        
        print("------ FIM DA LISTA ------")
        time.sleep(10)

    elif opcao == "3":
        agenda.clear()
        print("A agenda foi limpa!")
        time.sleep(TEMPO)

    elif opcao == "0":
        os.system("cls")
        print("Finalizando aplicação...")
        time.sleep(TEMPO)
        break # O freio de emergência!

    else:
        os.system("cls")
        print("Opção inválida, tente novamente!")
        time.sleep(TEMPO)