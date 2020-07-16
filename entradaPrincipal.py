import random
import time

global pessoasInternas


def contagemPessoas(vetor):

    lotacaoShopping = 500
    taxaPermitidaShopping = 0.3
    capMaxShopping = lotacaoShopping * taxaPermitidaShopping
    pessoasInternas = 14

    while capMaxShopping > pessoasInternas > 0:
        if vetor[0] == 1 and vetor[1] == 0:  # entrada de pessoas
            pessoasInternas = pessoasInternas + 1
            print("\nEntrada detectada! ")
            print("Quantidade de pessoas dentro do Shopping: ", pessoasInternas, "\n")
            teste = pessoasInternas
        time.sleep(3)

        if vetor[0] == 0 and vetor[1] == 1:  # saida de pessoas
            pessoasInternas = pessoasInternas - 1
            print("\nSaida detectada! ")
            print("Quantidade de pessoas dentro do Shopping: ", pessoasInternas)
            teste = pessoasInternas

        pessoasInternas = teste
        return str(pessoasInternas)