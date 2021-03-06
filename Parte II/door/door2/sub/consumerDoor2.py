import pika

# credentials = pika.PlainCredentials('scaps', '123456789')
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='door', exchange_type='fanout')

result = channel.queue_declare(queue='queue_door2', exclusive=False)
queue_door2 = result.method.queue
channel.queue_bind(exchange='door', queue=queue_door2)


def callback(ch, method, properties, body):
    print(" Detecção Porta 2: ", body)


channel.basic_consume(queue=queue_door2, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
