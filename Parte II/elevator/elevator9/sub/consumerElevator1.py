import pika

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='elevator', exchange_type='fanout')

result = channel.queue_declare(queue='queue_elevator1', exclusive=True)
queue_elevator1 = result.method.queue
channel.queue_bind(exchange='elevator', queue=queue_elevator1)


def callback(ch, method, properties, body):
    print(" Detecção Elevador 1: ", body)


channel.basic_consume(queue=queue_elevator1, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
