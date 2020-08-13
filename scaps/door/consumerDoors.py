import pika
import numpy as np

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='door', exchange_type='fanout')
n = 0


def consumerDoor():

    result = channel.queue_declare(queue='queue_door', exclusive=False)
    queue_door = result.method.queue
    channel.queue_bind(exchange='door', queue=queue_door)

    def callback(ch, method, properties, body):
        qntP1 = 0
        qntP2 = 0

        n = str(body)
        n1, n2, n3, n4 = n.split(', ')
        print(n1)
        n11 = n1.split("b'[(")
        print(n11)
        n1 = int(n1[4] + n1[5])
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4[0])
        print("Pessoas erradas: ", n1)
        print("Entradas: ", n2, type(n2))
        print("Saida", n3)
        print("Porta: ", n4, "\n")

        if n4 == 1:
            print("Porta 1: ", n1, "\n")
            qntP1 = n1

        if n4 == 2:
            print("Porta 2: ", n1, "\n")
            qntP2 = n1

        print("Quantidade Total: ", (50 + (qntP1 + qntP2)))


    channel.basic_consume(queue=queue_door, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumerDoor()