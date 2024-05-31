"""

# 45 - Exercício Final

## Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.

"""
times = {}

# Função para listar times
def listaTimes():
    print("Times listados:")
    for i, time in enumerate(times.values()):
        print(f"{i+1}. {time['nome']} ({len(time['jogadores'])} jogador) ")

# Função para listar jogadores
def listaJogadores(time):
    print(f"Jogadores do {time['nome']}:")
    for i, jogador in enumerate(time['jogadores']):
        print(f"{i+1}. {jogador}")

while True:

    print("""### Gerenciamento de Jogadores e Times ###

    Escolha uma opção abaixo:
    1- Adicionar time
    2- Remover time
    3- Listar times
    4- Adicionar jogador em um time
    5- Remover jogador em um time
    6- Listar jogadores de um time
    7- Encerrar programa
    """)




    opcao = int(input("Opção desejada:\n"))

    # Adiciona um time
    if opcao == 1:
        nomeTime = input("Informe o nome do Time:\n")
        times[nomeTime] = {'nome': nomeTime, 'jogadores': []}
        print("Time adicionado.")
    # Remove um time    
    elif opcao == 2:
        listaTimes()
        numeroTime = int(input("Informe o número do time que deseja remover: \n"))
        if numeroTime <= len(times):
            nomeTime = list(times.keys())[numeroTime-1]
            del times[nomeTime]
            print("Time removido.")
        else:
            print("Número invalido")
    # Listar Times   
    elif opcao == 3:
        listaTimes()
    elif opcao == 4:
        listaTimes()
        numeroTime = int(input("Informe o número do time que deseja adicionar jogador: "))
        if numeroTime <= len(times):
            nomeTime = list(times.keys())[numeroTime-1]
            nomeJogador = input("Informe o nome do jogador: ")
            times[nomeTime]['jogadores'].append(nomeJogador)
            print("Jogador adicionado no time.")
        else:
            print("Número do time inválido")
    elif opcao == 5:
        listaTimes()
        numeroTime = int(input("Informe o número do time que deseja adicionar jogador: "))
        if numeroTime <= len(times):
            nomeTime = list(times.keys())[numeroTime-1]
            listaJogadores(times[nomeTime])
            numeroJogador = int(input("Informe o número do jogador para remover: "))
            if numeroJogador <= len(times[nomeTime]['jogadores']):
                del times[nomeTime]['jogadores'][numeroJogador-1]
                print("Jogador removido do time.")
            else:
                print("Número do jogador inválido.")
        else:
            print("Número do time inválido")
    elif opcao == 6:
        listaTimes()
        numeroTime = int(input("Informe o número do time para listar jogadores: "))
        if numeroTime <= len(times):
            nomeTime = list(times.keys())[numeroTime-1]
            listaJogadores(times[nomeTime])
        else:
            print("Número do time inválido.")
    elif opcao == 7:
        print("Você encerrou o programa. Até a próxima!")
        break
    else:
         print("Opção invalida, informe uma existente!!!")
         

        
