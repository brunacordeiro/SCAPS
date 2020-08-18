import time
import random

lotacaoShopping = 5000
taxaPermitidaShopping = 0.3
capMaxShopping = lotacaoShopping * taxaPermitidaShopping

amountPeople = 50
amountEntry = 0
amountExit = 0
result = list()
porta = 2


def contagemPessoasDoor(vetor):  # [1,0] ... [0,1]

    global amountPeople
    global amountEntry
    global amountExit

    while amountPeople < capMaxShopping:

        if vetor[0] == 1 and vetor[1] == 0:  # entrada de pessoas
            print("\nEntrada detectada!")
            amountEntry = amountEntry + 1
            amountPeople = amountPeople + 1
            time.sleep(3)
            result = list()
            result.append((amountPeople, amountEntry, amountExit, porta))

        if vetor[0] == 0 and vetor[1] == 1:  # saida de pessoas
            print("\nSaida detectada! ")
            amountExit = amountExit + 1
            amountPeople = amountPeople - 1
            time.sleep(3)
            result = list()
            result.append((amountPeople, amountEntry, amountExit, porta))
            print(result)

        return str(result)

    exit()
