import pika
import time

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')

parameters = (
    pika.ConnectionParameters(host='localhost', port=5672, credenciats=credentials),
    pika.ConnectionParameters(host='localhost', port=5672, credenciats=credentials),
    pika.ConnectionParameters(host='localhost', port=5672, credenciats=credentials,
                              connection_attempts=5, retry_delay=1))
connection = pika.BlockingConnection(parameters)

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

lotacaoShopping = 5000
taxaPermitidaShopping = 0.3
capMaxShopping = lotacaoShopping * taxaPermitidaShopping


def consumer():
    result = channel.queue_declare(queue='queue_contagem', exclusive=False)
    queue_contagem = result.method.queue
    channel.queue_bind(exchange='contagem', queue=queue_contagem)

    def callback(ch, method, properties, body):
        global qntPessoas
        global qntPessoasEl, qntPessoasPt, qntPessoasEs
        global entElevador, saiElevador, entEscada, saiEscada, entPorta, saiPorta

        n = str(body)
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
        print("--------------------------------------------------------------------------")
        print("Entradas Totais:", (entEscada + entPorta + entElevador), "-> ",
              "Portas: ", entPorta, "\tEscadas: ", entEscada, "\tElevadores: ", entElevador)

        print("Saídas Totais:\t", (saiEscada + saiPorta + saiElevador), "-> ",
              "Portas: ", saiPorta, "\tEscadas: ", saiEscada, "\tElevadores: ", saiElevador)

        qntPessoas = (entEscada + entPorta + entElevador) - (saiEscada + saiPorta + saiElevador)
        entradas = (entEscada + entPorta + entElevador)
        saidas = (saiEscada + saiPorta + saiElevador)

        if qntPessoas > 0:
            print("\nTotal Pessoas no Shopping: ", qntPessoas, "\n")
            time.sleep(3)

            if qntPessoas > capMaxShopping:
                print("Lotação Máxima Atingida! \n")
                time.sleep(3)

        if qntPessoas < 0:
            print("\nShopping Vazio!\n")
            time.sleep(3)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_contagem, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
