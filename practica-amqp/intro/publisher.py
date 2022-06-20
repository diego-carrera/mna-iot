import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='4.tcp.ngrok.io', port=16738))
channel = connection.channel()

channel.queue_declare(queue='equipo43')

channel.basic_publish(exchange='', routing_key='equipo43', body='Hola Soy Diego 😈 🤘🏿 🫠 !')
print(" [x] Sent 'Hola Diego!'")
connection.close()
