import time
from random import randint

lotacaoShopping = 3000
taxaPermitidaShopping = 0.3
capMaxShopping = lotacaoShopping * taxaPermitidaShopping

amountWorker = 0
amountEntry = 0
amountExit = 0
result = list
loja = randint(1, 13)


def countWorker(vetor):  # [1,0] ... [0,1]

    global amountWorker
    global amountEntry
    global amountExit
    global loja
    global typeW

    while amountWorker < capMaxShopping:

        if vetor[0] == 1 and vetor[1] == 0:  # entrada de funcionarios
            print("\nEntrada detectada!")
            typeW = randint(21, 24)
            print("Categoria: ", catWorker(typeW))

            if typeW == 21 or typeW == 22:   # se funcionario loja ou prestador de serviço
                print("Loja: ", store(stores=loja))
                amountEntry = amountEntry + 1
                amountWorker = amountWorker + 1
                result = list()
                result.append((amountWorker, amountEntry, amountExit, loja))

            if typeW == 23:                            # se limpeza ou segurança
                amountEntry = amountEntry + 1
                amountWorker = amountWorker + 1
                result = list()
                result.append((amountWorker, amountEntry, amountExit, 30))

            if typeW == 24:                            # se limpeza ou segurança
                amountEntry = amountEntry + 1
                amountWorker = amountWorker + 1
                result = list()
                result.append((amountWorker, amountEntry, amountExit, 40))

        if vetor[0] == 0 and vetor[1] == 1:  # saida de pessoas
            print("\nSaida detectada! ")
            typeW = randint(21, 24)
            print("Categoria: ", catWorker(typeW))

            if typeW == 21 or typeW == 22:   # se funcionario loja ou prestador de serviço
                loja = randint(1, 12)
                print("Loja: ", store(stores=loja))
                amountExit = amountExit + 1
                amountWorker = amountWorker + 1
                result = list()
                result.append((amountWorker, amountEntry, amountExit, loja))

            if typeW == 23:  # se limpeza ou segurança
                amountExit = amountExit + 1
                amountWorker = amountWorker + 1
                result = list()
                result.append((amountWorker, amountEntry, amountExit, 30))

            if typeW == 24:  # se limpeza ou segurança
                amountExit = amountExit + 1
                amountWorker = amountWorker + 1
                result = list()
                result.append((amountWorker, amountEntry, amountExit, 40))

        #return str(result)

    exit()


def store(stores):
    switcher = {
        1: "C&A",
        2: "Renner",
        3: "Forever 21",
        4: "Zara",
        5: "Marisa",
        6: "Riachuelo",
        7: "Big Lar",
        8: "Americanas",
        9: "Pernambucanas",
        10: "Centauro",
        11: "Novo Mundo",
        12: "Polo Wear"
    }
    return switcher.get(stores, "Loja não cadastrada!")


def catWorker(category):
    switcher = {
        21: "Funcionário Loja",
        22: "Prestador de Serviço",
        23: "Equipe de Segurança",
        24: "Equipe de Limpeza"
    }
    return switcher.get(category, "Categoria de funcionário não cadastrada!")


def limitStore(limitWorker):
    switcher = {
        1: 25,
        2: 25,
        3: 20,
        4: 30,
        5: 20,
        6: 25,
        7: 20,
        8: 30,
        9: 20,
        10: 20,
        11: 20,
        12: 10,
        30: 20,
        40: 50
    }
    return switcher.get(limitWorker, "Não cadastrado!")
