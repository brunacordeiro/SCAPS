import pika
import time

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

entradas = 0
saidas = 0
qntPessoas = 0

entE1 = 0
entE2 = 0
entE3 = 0

saiE1 = 0
saiE2 = 0
saiE3 = 0


def consumerElevator():

    channel.exchange_declare(exchange='elevator', exchange_type='fanout')
    result = channel.queue_declare(queue='queue_elevator', exclusive=False)
    queue_elevator = result.method.queue
    channel.queue_bind(exchange='elevator', queue=queue_elevator)

    def callback(ch, method, properties, body):

        global entradas, saidas, qntPessoas
        global entE1, entE2, entE3, saiE1, saiE2, saiE3

        n = str(body)
        n1, n2, n3, n4 = n.split(', ')
        # n1 = int(n1[4] + n1[5])
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4[0])
        print("------------------------------------------------------------------")
        if n4 == 1:
            print("Informações Elevador: ", n4)
            print("Entradas: ", n2)
            print("Saida", n3)
            entE1 = n2
            saiE1 = n3

        if n4 == 2:
            print("Informações Elevador: ", n4)
            print("Entradas: ", n2)
            print("Saida", n3)
            entE2 = n2
            saiE2 = n3

        if n4 == 3:
            print("Informações Elevador: ", n4)
            print("Entradas: ", n2)
            print("Saida", n3)
            entE2 = n2
            saiE2 = n3

        entradas = entE1 + entE2 + entE3
        saidas = saiE1 + saiE2 + saiE3
        qntPessoas = entradas - saidas

        print("Entradas no Shopping: ", entradas)
        print("Saídas no Shopping: ", saidas)
        print("Quantidade de Pessoas dentro do Shopping:", qntPessoas)
        print("------------------------------------------------------------------\n")

        message = qntPessoas, "Elevador"
        channel.exchange_declare(exchange='contagem', exchange_type='fanout')
        channel.basic_publish(exchange='contagem', routing_key='', body=str(message))

    time.sleep(5)
    channel.basic_consume(queue=queue_elevator, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumerElevator()
