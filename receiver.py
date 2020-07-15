from typing import List, Any, Union

import pika
import sys
import time
import entradaPrincipal
import random


def connection():

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    entradaPrincipal.pessoasInternas = 14

    channel.exchange_declare(exchange='entradaShopping', exchange_type='fanout')

    # message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    while 1:
        message = entradaPrincipal.contagemPessoas(vetor=random.sample(range(2), 2))
        channel.basic_publish(exchange='entradaShopping', routing_key='', body=message)
        print(" [x] Sent %r" % message)
        time.sleep(3)

    connection.close()


if __name__ == "__main__":
    connection()