import time

lotacaoShopping = 5000
taxaPermitidaShopping = 0.3
capMaxShopping = lotacaoShopping * taxaPermitidaShopping

amountPeople = 0
amountEntry = 0
amountExit = 0
result = list()
escada = 1


def contagemPessoas(vetor):  # [1,0] ... [0,1]

    global amountPeople
    global amountEntry
    global amountExit

    while amountPeople < capMaxShopping:

        if vetor[0] == 1 and vetor[1] == 0:  # entrada de pessoas
            print("\nEntrada detectada Escada!")
            amountEntry = amountEntry + 1
            amountPeople = amountPeople + 1
            time.sleep(3)
            result = list()
            result.append((amountPeople, amountEntry, amountExit, escada))

        if vetor[0] == 0 and vetor[1] == 1:  # saida de pessoas
            print("\nSaida detectada Escada! ")
            amountExit = amountExit + 1
            amountPeople = amountPeople - 1
            time.sleep(3)
            result = list()
            result.append((amountPeople, amountEntry, amountExit, escada))

        return str(result)

    exit()
