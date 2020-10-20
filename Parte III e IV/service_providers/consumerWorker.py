import pika
import time
import controllerWorker

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='worker', exchange_type='fanout')

entradas = 0
saidas = 0
qntWorker = 0

ent = 0
saida = 0


def consumerWorker():

    result = channel.queue_declare(queue='queue_worker', exclusive=False)
    queue_worker = result.method.queue
    channel.queue_bind(exchange='worker', queue=queue_worker)

    def callback(ch, method, properties, body):

        global entradas, saidas, qntWorker
        global ent, saida

        n = str(body)
        # print(n)
        n1, n2, n3, n4 = n.split(', ')
        n2 = int(n2)
        n3 = int(n3)
        n41, n42 = n4.split(")]'")
        n4 = int(n41)
        loja = controllerWorker.store(n4)
        # print("------------------------------------------------------------------")

        if n4 == 1 and n2-n3 > 0:
            if n2-n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários na loja ", controllerWorker.store(1), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 2 and n2-n3 > 0:
            if n2-n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(2), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 3 and n2-n3 > 0:
            if n2-n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(3), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 4 and n2-n3 > 0:
            if n2-n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(4), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 5 and n2-n3 > 0:
            if n2-n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(5), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 6 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(6), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 7 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(7), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 8 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(8), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 9 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(9), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 10 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(10), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 11 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(11), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 12 and n2-n3 > 0:
            if n2 - n3 < controllerWorker.limitStore(n4):
                print("Qnt de funcionários loja ", controllerWorker.store(12), ": ", n2 - n3)
                ent = n2
                saida = n3
            else:
                print(loja, "Todos os funcionários estão presentes!")

        if n4 == 30 and n2-n3 > 0:
            print("Equipe de Segurança no Shopping: ", n2 - n3)
            ent = n2
            saida = n3

        if n4 == 40 and n2-n3 > 0:
            print("Equipe de Limpeza no Shopping: ", n2 - n3)
            ent = n2
            saida = n3

        qntWorker = ent - saida

        if qntWorker > 0:
            message = ent, saida, "Funcionarios"
            channel.exchange_declare(exchange='contagem', exchange_type='fanout')
            channel.basic_publish(exchange='contagem', routing_key='contagem', body=str(message))
            # print(message)

        else:
            print("Nenhum funcionário!")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_worker, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumerWorker()
