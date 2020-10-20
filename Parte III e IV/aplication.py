import pika
import time

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

channel = connection.channel()
channel.exchange_declare(exchange='contagem', exchange_type='fanout')

qntPessoas = 0
qntPessoasEl = 0
qntPessoasPt = 0
qntPessoasEs = 0
entElevador = 0
saiElevador = 0
entEscada = 0
saiEscada = 0
entPorta = 0
saiPorta = 0
entFunc = 0
saiFunc = 0

lotacaoShopping = 5000
lotacaoFuncionario = 1000
taxaPermitidaShopping = 0.3
capMaxShopping = lotacaoShopping * taxaPermitidaShopping


def consumer():
    result = channel.queue_declare(queue='', exclusive=False)
    queue_contagem = result.method.queue
    channel.queue_bind(exchange='contagem', queue='', routing_key='contagem')

    def callback(ch, method, properties, body):
        global qntPessoas
        global qntPessoasEl, qntPessoasPt, qntPessoasEs
        global entElevador, saiElevador, entEscada, saiEscada, entPorta, saiPorta
        global entFunc, saiFunc

        n = str(body)
        #   print (n)
        a, sai, c = n.split(', ')
        a, ent = a.split('b"(')
        local, d = c.split(')"')
        # print("Entradas: ", ent, "\t Saídas: ", sai, "\t Local: ", local)
        ent = int(ent)
        sai = int(sai)

        if local == "'Portas'":
            entPorta = ent
            saiPorta = sai

        if local == "'Elevador'":
            entElevador = ent
            saiElevador = sai

        if local == "'Escada'":
            entEscada = ent
            saiEscada = sai

        if local == "'Funcionarios'":
            entFunc = ent
            saiFunc = sai

        print("-------------------------------------------------------------------------------")
        print("Entradas Clientes:\t", (entEscada + entPorta + entElevador), "-> ",
              "Portas: ", entPorta, "\tEscadas: ", entEscada, "\tElevadores: ", entElevador)

        print("Saídas Clientes: \t", (saiEscada + saiPorta + saiElevador), "-> ",
              "Portas: ", saiPorta, "\tEscadas: ", saiEscada, "\tElevadores: ", saiElevador)

        print("\nEntradas Funcionários: ", entFunc, "\t Saídas Funcionários: ", saiFunc)

        qntPessoas = (entEscada + entPorta + entElevador) - (saiEscada + saiPorta + saiElevador)
        entradas = (entEscada + entPorta + entElevador + entFunc)
        saidas = (saiEscada + saiPorta + saiElevador + saiFunc)

        if qntPessoas > 0:
            print("\nTotal -> Pessoas no Shopping: ", qntPessoas, "\t Funcionários no Shopping: ", entFunc-saiFunc, "\n")
            time.sleep(3)

            if qntPessoas > capMaxShopping:
                print("Lotação Máxima Atingida! \n Por favor aguarde alguns minutos...")
                time.sleep(3)

            if entFunc-saiFunc > lotacaoFuncionario:
                print("Lotação Máxima de Funcionários Atingida! \n Verifique seu horário de entrada!")

        if qntPessoas < 0:
            print("\nShopping Vazio!\n")
            time.sleep(3)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_contagem, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
