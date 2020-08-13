from typing import List, Any, Union

import pika
import sys
import time
import entradaPrincipal
import random


def connection():

    # credentials = pika.PlainCredentials('scaps', '123456789')
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='door', exchange_type='fanout')
    channel.exchange_declare(exchange='elevator', exchange_type='fanout')
    channel.exchange_declare(exchange='ladder', exchange_type='fanout')


    while 1:

        for porta in range(2):
            message_p1 = entradaPrincipal.contagemPessoas(vetor=random.sample(range(2), 2))  #[1,0]
            channel.basic_publish(exchange='door', routing_key='', body=message_p1)
            time.sleep(3)

        for elevador in range(10):
            message_el = entradaPrincipal.contagemPessoas(vetor=random.sample(range(2), 2))  # [1,0]
            channel.basic_publish(exchange='elevator', routing_key='', body=message_el)
            time.sleep(3)

        for escada in range(8):
            message_e1 = entradaPrincipal.contagemPessoas(vetor=random.sample(range(2), 2))  # [1,0]
            channel.basic_publish(exchange='ladder', routing_key='', body=message_e1)
            time.sleep(3)


    connection.close()


if __name__ == "__main__":
    connection()
