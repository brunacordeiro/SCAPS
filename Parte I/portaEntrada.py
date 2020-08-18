from datetime import datetime, timedelta
import random

lotacaoShopping = 5000
taxaPermitidaShopping = 0.3
capMaxShopping = 50  # só para testar com um número menor do que o real
# capMaxShopping = lotacaoShopping * taxaPermitidaShopping
# quantEntradasDisponiveis = 1 (para quando formos trabalhar com várias entradas)
statusShopping = 1  # quer dizer que shopping aberto

inicio = datetime.now()
data_hora = []
entrada_saida = []
qtde = 50  # define um número inicial de pessoas

i = 0

while statusShopping == 1:
    for i in range(0,5): # caso queira executar só 5 vezes para ver o que acontece linha a linha, só comentar a de cima e descomentar essa
        data_hora_gerada = inicio + timedelta(minutes=i)
        #i += 1  # se for usar o for para ver, comenta essa também
        # print (data_hora_gerada)
        data_hora.append(data_hora_gerada)
        situacao = random.randint(0, 1)
        # print (situacao)

    if situacao == 1 and qtde < capMaxShopping:
        print("Quantidade de pessoas permitidas: %i" % capMaxShopping)
        print("Quantidade de pessoas no Shopping: %i" % qtde)
        qtde += 1
        print("Entrada permitida!")
        print("Quantidade de pessoas (atualizado): %i" % qtde)
        print("\n")
        entrada_saida.append(situacao)
    elif situacao == 1 and qtde >= capMaxShopping:
        print("Quantidade de pessoas permitidas: %i" % capMaxShopping)
        print("Quantidade de pessoas no Shopping: %i" % qtde)
        print("Capacidade máxima excedida: entrada não permitida!")
        print("\n")
    else:
        print("Quantidade de pessoas permitidas: %i" % capMaxShopping)
        print("Quantidade de pessoas no Shopping: %i" % qtde)
        qtde -= 1
        print("Saída realizada!")
        print("Quantidade de pessoas (atualizado): %i" % qtde)
        print("\n")
        entrada_saida.append(situacao)
# print(data_hora)
# print(qtde)
print(entrada_saida) # se quiser ver esse vetor com os dados gravados, só descomentar
