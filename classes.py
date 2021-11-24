import Confirmar
#Cadastro dos candidatos à Governador
nameGov1 = ('1: Zidane')
nameGov2 = ('2: Ronaldo')
nameGov3 = ('3: Papadopoulos')
nameGov4 = ('4: Guillit')
nameGov5 = ('5: Beckenbauer')

#Cadastro dos candidatos à Presidência
namePres1 = ('1: João Vitor')
namePres2 = ('2: Roberto')
namePres3 = ('3: Eduardo')
namePres4 = ('4: Pedro')
namePres5 = ('5: Danilo')

#Menu da Urna
def menuUrna():
    print('Urna Eletrônica 4.0')
    print('-'*30)
    print('1: Listar Candidatos')
    print('2: Iniciar Votação')
    print('3: Apurar votos')
    print('4: Desligar urna')
    print('-'*30)
    

def opMenu():
    return(int(input("Digite a opção desejada: ")))


def votarPres():
    votePres = input("\nDigite a opção de voto à Presidência ou vote em Branco (B ou b): ")


    if votePres == 'B' or votePres == 'b':
        print("Voto em Branco registrado!")

        if Confirmar.confirmarVoto():
            Resultado.votoEmBrancoPres += 1
        
    elif votePres == '1':
        print(f"\nCandidato escolhido: {namePres1}")

        if Confirmar.confirmarVoto():
            Resultado.votoPres1 += 1

    elif votePres == '2':
        print(f"\nCandidato escolhido: {namePres2}")

        if Confirmar.confirmarVoto():
            Resultado.votoPres2 += 1
        
    elif votePres == '3':
        print(f"\nCandidato escolhido: {namePres3}")

        if Confirmar.confirmarVoto():
            Resultado.votoPres3 += 1

    elif votePres == '4':
        print(f"\nCandidato escolhido: {namePres4}")

        if Confirmar.confirmarVoto():
            Resultado.votoPres4 += 1

    elif votePres == '5':
        print(f"\nCandidato escolhido: {namePres5}")

        if Confirmar.confirmarVoto():
            Resultado.votoPres5 += 1

    else:
            presNulo.nuloPres()

def votarGov():
    voteGov = input("\nDigite o número do candidato à governador (ou B para Em Branco): ").upper()

    if voteGov == 'B':
        print("\nVoto em Branco Registrado!")

        if Confirmar.confirmarVoto():
            Resultado.votoEmBrancoGov += 1
      
    elif voteGov == '1':
        print(f"\nCandidato escolhido: {nameGov1}")
        
        if Confirmar.confirmarVoto():
            Resultado.voteGov1 += 1

    elif voteGov == '2':
        print(f"\nCandidato escolhido: {nameGov2}")
        
        if Confirmar.confirmarVoto():
            Resultado.voteGov2 += 1

    elif voteGov == '3':
        print(f"\nCandidato escolhido: {nameGov3}")
        
        if Confirmar.confirmarVoto():
            Resultado.voteGov3 += 1
        
    elif voteGov == '4':
        print(f"\nCandidato escolhido: {nameGov4}")
        
        if Confirmar.confirmarVoto():
            Resultado.voteGov4 += 1

    elif voteGov == '5':
        print(f"\nCandidato escolhido: {nameGov5}")
        
        if Confirmar.confirmarVoto():
            Resultado.voteGov5 += 1

    else:
        govNulo.nuloGov()  



def listaCandidatos():
    print('\nCandidatos a Presidência')
    print ("\n", namePres1, "\n", namePres2, "\n", namePres3, "\n", namePres4, "\n", namePres5)

    print('\nCandidatos a Governador')
    print("\n", nameGov1, "\n", nameGov2, "\n", nameGov3, "\n", nameGov4, "\n", nameGov5)




#Guardar Votação
voteGov1 = 0
voteGov2 = 0
voteGov3 = 0
voteGov4 = 0
voteGov5 = 0

votePres1 = 0
votePres2 = 0
votePres3 = 0
votePres4 = 0
votePres5 = 0

nuloGov = 0
nuloPres = 0

brancoGov = 0 
brancoPres = 0


def Resultado():
    
        #Resultado Governador:

        print("\n Total da votação à Governador:")
        print(" O candidato 1:", voteGov1, "votos.")
        print(" O candidato 2:", voteGov2, "votos.")
        print(" O candidato 3:", voteGov3, "votos.")
        print(" O candidato 4:", voteGov4, "votos.")
        print(" O candidato 5:", voteGov5, "votos.")
        print(" Votos em Branco para Governador:", brancoGov, "votos.")
        print(" Votos Nulos para Governador:", nuloGov, "votos.")

        #Resultado à Presidência:
        print ("\nTotal da votação à Presidente:")
        print ("O candidato 1", votePres1, "votos.")
        print ("O candidato 2", votePres2, "votos.")
        print ("O candidato 3", votePres3, "votos.")
        print ("O candidato 4", votePres4, "votos.")
        print ("O candidato 5", votePres5, "votos.")
        print ("Votos em Branco para Presidente", brancoPres, "votos.")
        print ("Votos em Nulos para Presidente", nuloPres, "votos.")


#Votos nulos ou Brancos
def govNulo():
    anularGov = 0 
    anular = input("\nDeseja votar nulo? (s ou n): ").lower()
    
    if anular == "s":
        print("\nVoto nulo registrado!")
        anularGov += 1

    elif anular == "n":
        print("\nVoto nulo não registrado!")

    else:
        print("\nOpção inválida!")

def presNulo():        
    anularPress = 0 
    anular = input("\nDeseja votar nulo? (s ou n): ").lower()
    
    if anular == "s":
        print("\nVoto nulo registrado!")
        anularPress += 1

    elif anular == "n":
        print("\nVoto nulo não registrado!")

    else:
        print("\nOpção inválida!")