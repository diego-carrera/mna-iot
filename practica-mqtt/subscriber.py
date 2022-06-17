#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqttClient

def on_connect(client, userdata, flags, rc):
  """
  On connect
  :param client:
  :param userdata:
  :param flags:
  :param rc:
  :return:
  """
  if rc == 0:
    print("Connected with result code " + str(rc))
    global Connected
    Connected = True
  else:
    print("Bad connection Returned code=", rc)
    Connected = False


def on_message(client, userdata, message):
    print("Message received: {message.topic} - {message.payload}".format(message=message))
    return

Connected = False
broker_address="broker.hivemq.com"
broker_port=1883

tag = "/MNA/IoT/CompProf/#"

client = mqttClient.Client("ClienteEquipo43")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)
client.loop_start()

while Connected != True:
  time.sleep(0.1)
  client.subscribe(tag)

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    print("Exiting")
    client.disconnect()
    client.loop_stop()

