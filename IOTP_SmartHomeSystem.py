from urllib.parse import urlparse
import paho.mqtt.client as paho
import os,sys
import time
import smbus2
import bme280
import json

from gpiozero import LED, OutputDevice, Buzzer
from time import sleep

led = LED(17)
fan = OutputDevice(25)
buzzer = Buzzer(21)

port = 1
address = 0x76

bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data= bme280.sample(bus, address, calibration_params)

def on_connect(self, mosq, obj, rc):
    self.subscribe("Air-Con",0)

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(msg.payload == b"on"):
        print("Air-Con on")
        led.on()
        time.sleep(5)
    elif(msg.payload== b"off"
        print("Air-Con off")
        led.off()
    else:
        print("Air-Con off")
        led.off()
        time.sleep(5)
        
def on_publish(mosq, obj, mid):
    print("mid: "+str(mid))
    
def on_subscribe(mosq, obj,mid,granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

sensor_data={ 'Temperature': 0, 'Humidity' : 0} # for thingsboard dashboard
client= paho.Client()
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

url_str = os.environ.get('CLOUD_MQTT_URL', "tcp://broker.emqx.io:1883")
url = urlparse(url_str)
mqttc.connect(url.hostname, url.port)
print("MQTT Connected")

iot_hub="demo.thingsboard.io"
port= 1883
username ="krspxqEH2BAqKiSueXbG"
password=""
topic="v1/devices/me/telemetry"
client.username_pw_set(username,password)
url_str = os.environ.get('CLOUD_MQTT_URL', 'tcp://broker.emqx.io:1883') 
url = urlparse(url_str)
mqttc.connect(url.hostname, url.port)
client.connect(iot_hub,port,60)
print("ThingBoard Connected")

rc=0
Tb=0
bz = 0
data.temperature = int(data.temperature)
data.humidity = int(data.humidity)
while rc == 0 and Tb== 0:
    rc=mqttc.loop()
    Tb=client.loop()
    if data.temperature is not None and data.humidity is not None:
        print('Temp={0:0.2f}*c Humidity ={1:0.2f}%'.format(data.temperature,data.humidity))
        mqttc.publish("temperature",str(data.temperature))# to mobile app
        mqttc.publish("humidity",str(data.humidity))# to mobile app
        sensor_data['Temperature'] = data.temperature # to thingboard dashboard         		 sensor_data['Humidity'] = data.humidity # to thingboard dashboard         	  sensorOut=json.dumps(sensor_data) # to thingboard dashboard
        client.publish(topic,sensorOut,1) # to thingboard dashboard
        time.sleep(1)
    else:
        print("Failed to get reading.Try again!")
        
    if data.temperature > 20 and data.humidity > 40:
        print("All appliances turned on")
        mqttc.publish("alert", "data.temperature")# to mobile app
        led.on()
        fan.on()
        buzzer.on()
        bz = bz + 1
        if bz > 1:
            buzzer.off()
            continue
        
        
    elif (data.temperature > 20 and data.temperature < 25):
        fan.on()
        led.off()
        bz == 0
        print("Fan is turned on")
        
    elif (data.humidity > 50 and data.humidity < 70 ):
        fan.off()
        led.on()
        bz == 0 
        print("Air-con is turned on")
    else:
        fan.off()
        led.off()
        bz == 0
        print("All appliances off")        
