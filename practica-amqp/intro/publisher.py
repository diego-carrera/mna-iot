#!/usr/local/env python
# -*- coding: utf-8 -*-

import time
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='equipo43')
try:
  i = 0
  while True:
    message =  "%5d Hola Soy Diego 😈 🤘🏿 " % i
    channel.basic_publish(exchange='', routing_key='equipo43', body=message)
    print(" [x] Sent 'Hola Diego!'")
    time.sleep(0.1)
    i = i + 1
except KeyboardInterrupt:
  pass

connection.close()
