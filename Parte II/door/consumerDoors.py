import pika
import time

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='door', exchange_type='fanout')

entradas = 0
saidas = 0
qntPessoas = 0

entP1 = 0
entP2 = 0
entP3 = 0

saiP1 = 0
saiP2 = 0
saiP3 = 0


def consumerDoor():

    result = channel.queue_declare(queue='queue_door', exclusive=False)
    queue_door = result.method.queue
    channel.queue_bind(exchange='door', queue=queue_door)

    def callback(ch, method, properties, body):

        global entradas, saidas, qntPessoas
        global entP1, entP2, entP3, saiP1, saiP2, saiP3

        n = str(body)
        n1, n2, n3, n4 = n.split(', ')
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4[0])
        print("------------------------------------------------------------------")

        if n4 == 1:
            print("Informações Porta: ", n4)
            print("Entradas: ", n2)
            print("Saida", n3)
            entP1 = n2
            saiP1 = n3

        if n4 == 2:
            print("Informações Porta: ", n4)
            print("Entradas: ", n2)
            print("Saida", n3)
            entP2 = n2
            saiP2 = n3

        if n4 == 3:
            print("Informações Porta: ", n4)
            print("Entradas: ", n2)
            print("Saida", n3)
            entP3 = n2
            saiP3 = n3

        entradas = entP1 + entP2 + entP3
        saidas = saiP1 + saiP2 + saiP3
        qntPessoas = entradas - saidas

        print("Entradas no Shopping: ", entradas)
        print("Saídas no Shopping: ", saidas)
        print("Quantidade de Pessoas dentro do Shopping:", qntPessoas)
        print("------------------------------------------------------------------\n")

        message = entradas, saidas, "Portas"
        channel.exchange_declare(exchange='contagem', exchange_type='fanout')
        channel.basic_publish(exchange='contagem', routing_key='', body=str(message))

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_door, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumerDoor()
