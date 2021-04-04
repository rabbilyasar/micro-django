import pika

params = pika.URLParameters('amqps://peapkxkh:ov3PISTScVbVHJaMxtrCQRnGFd3SqEDP@gull.rmq.cloudamqp.com/peapkxkh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')