import pika

params = pika.URLParameters('amqps://peapkxkh:ov3PISTScVbVHJaMxtrCQRnGFd3SqEDP@gull.rmq.cloudamqp.com/peapkxkh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()
channel.close()