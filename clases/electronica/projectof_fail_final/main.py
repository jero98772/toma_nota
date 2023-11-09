import subprocess
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
# comment and uncomment the lines below depending on your sensor
sensor = Adafruit_DHT.DHT11
addr="localhost"
port=1883
pin=21
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin,GPIO.OUT)

# sensor = Adafruit_DHT.DHT11
client=mqtt.Client()
client.connect(addr,port)
# DHT pin connects to GPIO 4
sensor_pin =4
topic1="humidity"
topic2="temperatureF"
topic3="led"
print("ff")
def on_message(client,userdata,message):
    dato=message.payload.decode()
    if dato=="on":
        GPIO.output(pin,GPIO.HIGH)
        print("onnnkkknnn")
        time.sleep(3)
    else:
         GPIO.output(pin,GPIO.LOW)
         print("offf")
    print(message.topic,message.payload.decode())
client.loop_start()
client.on_message=on_message
while True:
    print("ff")

    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)  # Use read_retry to retry in case of failure
    print("ff")

    if humidity is not None and temperature is not None:
        # Uncomment the line below to convert to Fahrenheit
        
        temperatureF = temperature * 9/5.0 + 32
        client.publish(topic1,humidity)
        client.publish(topic2,temperatureF)
        #subprocess.run("mosquitto_pub -d -t "+topic1+" -m "+str(humidity),shell=True)
        #subprocess.run("mosquitto_pub -d -t "+topic2+" -m "+str(temperatureF),shell=True)
        

        print(temperature, temperatureF, humidity)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(1)
    print(client.subscribe(topic3),"topic")
#client.loop_forever()  
#https://randomnerdtutorials.com/raspberry-pi-dht11-dht22-python/
#https://iot.stackexchange.com/questions/3397/view-the-messages-sent-to-the-local-mosquitto-server
"""
publicar
mosquitto_pub -d -t humidity 
mosquitto_pub -d -t temperatureF
subscripcion

mosquitto_sub -h localhost -t humidity
mosquitto_sub -h localhost -t temperatureF

"""