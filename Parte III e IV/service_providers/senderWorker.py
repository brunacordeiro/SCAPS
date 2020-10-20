import pika
import time
import random
import controllerWorker


def worker():

    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='worker', exchange_type='fanout')
    channel = connection.channel()

    while 1:

        message = controllerWorker.countWorker(vetor=(random.sample(range(2), 2)))  # [1,0]
        print(message)
        channel.basic_publish(exchange='worker', routing_key='', body=message)
        time.sleep(5)

    connection.close()


if __name__ == '__main__':
    worker()
