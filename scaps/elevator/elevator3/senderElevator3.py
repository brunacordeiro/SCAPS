import pika
import time
import random
import controllerElevator


def elevator3():
    # credentials = pika.PlainCredentials('scaps', '123456789')
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='elevator', exchange_type='fanout')
    channel = connection.channel()

    while 1:

        message = controllerElevator.contagemPessoas(vetor=random.sample(range(2), 2))  # [1,0]
        channel.basic_publish(exchange='elevator', routing_key='', body=message)
        print("Elevador ", ": %r \n" % message)
        time.sleep(5)

    connection.close()


if __name__ == '__main__':
    elevator3()
