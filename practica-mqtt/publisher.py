#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import time
import paho.mqtt.client as mqttClient
import simplejson as json

dataframe = pd.read_csv("DatosPruebaMQTT.csv", index_col=0)

df = dataframe.dropna()
temp = df.Temperature.tolist()
co = df.CO2.tolist()
hum = df.Humidity.tolist()

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

Connected = False
broker_address="broker.hivemq.com"
broker_port=1883

temp_tag = "/MNA/IoT/Equipo43/Temp"
hum_tag = "/MNA/IoT/Equipo43/Humedad"
co2_tag = "/MNA/IoT/Equipo43/Co2"

client = mqttClient.Client("ClienteEquipo43")
client.on_connect = on_connect
client.connect(broker_address, broker_port)
client.loop_start()


while Connected != True:
  time.sleep(0.1)
  try:
    for i,j,k in zip(temp,co,hum):

      tempPayload = json.dumps({"Temperature": i})
      co2Payload = json.dumps({"CO2": j})
      humPayload = json.dumps({"CO2": k})

      print("Publishing to topic {0} {1}".format(temp_tag, tempPayload))
      print("Publishing to topic {0} {1}".format(co2_tag, co2Payload))
      print("Publishing to topic {0} {1}".format(hum_tag, humPayload))

      client.publish(temp_tag, tempPayload)
      client.publish(co2_tag, co2Payload)
      client.publish(hum_tag, humPayload)

      time.sleep(2)

  except KeyboardInterrupt:
    print("Finished")
    client.disconnect()
    client.loop_stop()
    print("Finished")



