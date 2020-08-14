import time
import random

lotacaoShopping = 5000
taxaPermitidaShopping = 0.3
capMaxShopping = lotacaoShopping * taxaPermitidaShopping
amountPeople = 50
amountDoor = 0
amountElevator = 0
amountLadder = 0
amountDoorExit = 0
amountElevatorExit = 0
amountLadderExit = 0


def contagemPessoas(vetor):  # [1,0] ... [0,1]

    global amountPeople
    global amountDoor
    global amountElevator
    global amountLadder
    global amountDoorExit
    global amountElevatorExit
    global amountLadderExit

    while amountPeople < capMaxShopping:

        if amountPeople > 0:
            if vetor[0] == 1 and vetor[1] == 0:  # entrada de pessoas
                deteccaoEntrada = random.randint(1, 3)

                if deteccaoEntrada == 1:   # Entrada por uma Porta
                    print("\nEntrada detectada na Porta: ", random.randint(1, 2))
                    amountDoor = amountDoor + 1
                    amountPeople = amountPeople + 1

                if deteccaoEntrada == 2:  # Entrada por um Elevador
                    print("\nEntrada detectada no Elevador: ", random.randint(1, 10))
                    amountElevator = amountElevator + 1
                    amountPeople = amountPeople + 1

                if deteccaoEntrada == 3:  # Entrada por uma Escada
                    print("\nEntrada detectada na Escada: ", random.randint(1, 8))
                    amountLadder = amountLadder + 1
                    amountPeople = amountPeople + 1

            time.sleep(3)

            if vetor[0] == 0 and vetor[1] == 1:  # saida de pessoas
                deteccaoSaida = random.randint(1, 3)

                if deteccaoSaida == 1:  # Entrada por uma Porta
                    print("\nSaida detectada na Porta: ", random.randint(1, 2))
                    amountDoorExit = amountDoorExit + 1
                    amountPeople = amountPeople - 1

                if deteccaoSaida == 2:  # Entrada por um Elevador
                    print("\nSaida detectada no Elevador: ", random.randint(1, 10))
                    amountElevatorExit = amountElevatorExit + 1
                    amountPeople = amountPeople - 1

                if deteccaoSaida == 3:  # Entrada por uma Escada
                    print("\nSaida detectada na Escada: ", random.randint(1, 8))
                    amountLadderExit = amountLadderExit + 1
                    amountPeople = amountPeople - 1

            print("\n------------------Informações Entrada e Saída ----------------------------------")
            print("Entrada Portas: ", amountDoor, "\t\t\tSaída Portas: ", amountDoorExit)
            print("Entrada Elevadores: ", amountElevator, "\t\tSaída Elevadores: ", amountElevatorExit)
            print("Entrada Escadas: ", amountLadder, "\t\tSaída Escadas: ", amountLadderExit)

            print("\nQuantidade de pessoas que entraram: ", amountDoor + amountElevator + amountLadder)
            print("Quantidade de pessoas que sairam: ", amountDoorExit + amountElevatorExit + amountLadderExit)
            print("---------------------------------------------------------------------------------")

            print("\nQuantidade Total dentro do Shopping", amountPeople, "\n\n\n")

            return str(amountPeople)
        else:
            
            print("Shopping está vazio!")

    print("\nCapacidade Máxima Atingida")

    exit()
