from classes import*



#Opções do Menu
opcao = 0

while opcao != 4:

    menuUrna()
    opcao = opMenu()

    if opcao == 1:
        listaCandidatos() #lista dos candidatos

    elif opcao == 2:
        votarGov()
        votarPres()

    elif opcao == 3:
        Resultado() #menu da apuração

    elif opcao == 4:
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")
        
    else:
        print("\nOpção inválida!") #opção caso o usuário digite uma opção incorreta do menu