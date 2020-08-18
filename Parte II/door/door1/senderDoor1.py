import pika
import time
import random
import door.door1.controllerDoor as controllerDoor


def door1():
    # credentials = pika.PlainCredentials('scaps', '123456789')
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='door', exchange_type='fanout')
    channel = connection.channel()

    while 1:

        message = controllerDoor.contagemPessoasDoor(vetor=random.sample(range(2), 2))  # [1,0]
        channel.basic_publish(exchange='door', routing_key='', body=message)
        print("Porta ", ": %r \n" % message)
        time.sleep(5)

    connection.close()


if __name__ == '__main__':
    door1()
