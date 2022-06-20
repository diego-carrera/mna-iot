#!/usr/bin/env python
from datetime import datetime
from random import randint
import time
import pika
import sys

connection = pika.BlockingConnection(
  pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

try:
  i = 0
  message_no = 1

  personas = ['Lex', 'Ismael', 'Sebastian', 'Diego']
  while True:

    nombre = personas[i]

    message = "#{0} - Hola {1}!, {2}".format(message_no, nombre, datetime.now())
    channel.basic_publish(
      exchange='',
      routing_key='task_queue',
      body=message,
      properties=pika.BasicProperties(
          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
      )
    )
    print(" [x] Sent %r" % message)
    time.sleep(0.5)
    i = i + 1
    message_no = message_no + 1
    if  i >= len(personas):
      i = 0

except KeyboardInterrupt:
  pass

connection.close()
