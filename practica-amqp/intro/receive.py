#!/usr/local/env python
# -*- coding: utf-8 -*-

import pika, sys, os

def main():
  connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()

  channel.queue_declare(queue='equipo43')

  def callback(ch, method, properties, body):
    print(" [x] Recibí mensaje %r " % body.decode('UTF-8'))

  channel.basic_consume(queue='equipo43', on_message_callback=callback, auto_ack=True)

  print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()

main()
