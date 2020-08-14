import pika
import time

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='contagem', exchange_type='fanout')

qntPessoas = 0
qntPessoasEl = 0
qntPessoasPt = 0
qntPessoasEs = 0
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

        n = str(body)
        a, qnt = n.split('b"(')
        qnt, b = qnt.split(')"')
        qnt, c = qnt.split(', ')
        qnt = int(qnt)
        # print("Contagem local: ", qnt, "\nLocal: ", c)

        if c == "'Elevador'":
            qntPessoasEl = qnt + qntPessoasEl
            # print("elevador", qntPessoasEl)
        if c == "'Portas'":
            qntPessoasPt = qnt + qntPessoasEl
            # print("portas", qntPessoasPt)
        if c == "'Escada'":
            qntPessoasEs = qnt + qntPessoasEs
            # print("escada", qntPessoasEs)

        qntPessoas = qntPessoasPt + qntPessoasEl + qntPessoasEs

        if qntPessoas > 0:
            print("\n Total Pessoas no Shopping: ", qntPessoas)

            if qntPessoas > capMaxShopping:
                print("Lotação Máxima Atingida!")

    channel.basic_consume(queue=queue_contagem, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
