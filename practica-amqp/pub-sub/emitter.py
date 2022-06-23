#!/usr/local/env python

from datetime import datetime
import time
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

try:
  i = 0
  message_no = 1
  while True:
    personas = ['Lex', 'Ismael', 'Sebastian', 'Diego']
    nombre = personas[i]

    message = "#{0} - Hola {1}!, {2}".format(message_no, nombre, datetime.now())
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    # print(" [x] Sent %r" % message)
    time.sleep(0.5)
    i = i + 1
    message_no = message_no + 1
    if  i >= len(personas):
      i = 0

except KeyboardInterrupt:
  pass

connection.close()
