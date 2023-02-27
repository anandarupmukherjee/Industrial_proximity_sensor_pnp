
import time
import paho.mqtt.client as mqtt
import json
import automationhat



# Read automation hat input channel and activate based on input from the OMRON proximity sensor
if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

print("Initiating transmission over MQTT")
mqttc = mqtt.Client()
print("Done. Listening on the local docker network....")


while True:
    dat=automationhat.input.read()
    print(dat["one"])
    c={"s1":dat["one"]}
    msg=json.dumps(c)
    mqttc.connect("172.18.0.4", 1883, 60)
    mqttc.publish("Boeing/Maintenance/IBC1",payload=msg)
    #print("Time transmitted to local network....")
    # mqttc.loop_forever()
    print('Publish End')
    if dat["one"]==0:
        automationhat.relay.one.toggle()
        automationhat.relay.two.toggle() 
        automationhat.relay.three.toggle()     
    #print(automationhat.analog.read())
    time.sleep(0.5)

