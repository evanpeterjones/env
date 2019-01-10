import RPi.GPIO as gpio
import Adafruit_DHT as dht
import os
import time

gpio.setmode(gpio.BCM)
power = 4
data  = 24
gpio.setup(power, gpio.OUT)
gpio.output(power, gpio.HIGH)

minTemp  = 50
minHumid = 60

#humidity, temp = dht.read_retry(dht.AM2302, 9)
humidity, temp = dht.read_retry(dht.AM2302, data)
if temp is None and humidity is None:
    print("no data")
else:
    # convert to Farenheit
    temp = temp * (9/5)+32
    print("Temperature: "+str(temp))
    print("Humidity: "+str(humidity))

def humidifer(command):
    os.system("curl -X POST https://maker.ifttt.com/trigger/"+command+"/with/key/iuqTik_MlP-QhXazswBCAG_FJZCDFQyFEJRR7Lk4NeS")
    print("\nhumidifier set to " + command)

while humidity is not None:
    if (humidity < minHumid):
        humidifer("humidifier-on")
    if (humidity > minHumid) :
        humidifer("humidifier-off")
    humidity = None

gpio.cleanup()
