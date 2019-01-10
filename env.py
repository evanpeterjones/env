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
heaterState   = "heater-off"
humidityState = "humidifier-off"

class env:
    def __init__(self):
        humidity, temp = 0
        time = ""        

    @property
    def temperature(self):
        return temp

    @property
    def humidity(self):
        return humidity

    def read(self):
        humidity, temp = dht.read_retry(dht.AM2302, data)

        if temp is None and humidity is None:
            print("no data")
        else:
            temp= temp * (9/5)+32
            print("data collected")
        return (humidity, temp)

    def humidifier(self, command):
        if command is not humidityState: # and location is home
            os.system("curl -X POST https://maker.ifttt.com/trigger/"+
                      command+"/with/key/iuqTik_MlP-QhXazswBCAG_FJZCDFQyFEJRR7Lk4NeS")
            print("\nhumidifier set to " + command)
        else:
            print("no change state")

    def loop(self):
        while humidity is not None and temp is not None:
            if (humidity < minHumid):
                humidifier("humidifier-on")
            if (humidity > minHumid):
                humidifier("humidifier-off")
            # humidity = None
            # temp = None
            time.sleep(600)

if __name__ == "__main__":
    room = env()
    print(room.temperature)
    gpio.cleanup()
