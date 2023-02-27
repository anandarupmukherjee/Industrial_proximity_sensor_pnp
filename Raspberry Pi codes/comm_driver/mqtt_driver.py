#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import os
import time as t
import json
import re



t.sleep(2)

def insert_val(x,s1,loc): 
    dev="amco"
    var="curl -i -XPOST 'http://172.18.0.2:8086/write?db=ev' --data 'sensor1 x="+str(x)+"',x_stat="+str(s1)+"',z="+str(x)+"'"
    os.system(var)






def on_message_pnp(mosq, obj, msg):
    print("entered loop")
    top=msg.topic
    print(top)
    data = "{}".format(str(msg.payload,"utf-8"))
    print(data)
    data1=json.loads(data)
    x1=data1["s1"]

    if x1==0:
        s1_status=1
    else:
        s1_status=0

    insert_val(x1,s1_status,top)



def on_message(mosq, obj, msg):
    print("entered loop")
    top=msg.topic
    data = "{}".format(msg.payload)
    message = {"message":data}
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))



print("Edge handshake initiate...")
mqttc = mqtt.Client()
print("Done. Listening on the local network....")

# Add message callbacks that will only trigger on a specific subscription match.

mqttc.message_callback_add("Boeing/Maintenance/IBC1", on_message_pnp)
mqttc.on_message = on_message
mqttc.connect("172.18.0.4", 1883, 60)
mqttc.subscribe("Boeing/Maintenance/#", 0)
mqttc.loop_forever()
print('Publish End')
