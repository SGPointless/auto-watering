# Automatic plant watering
import logging
import time
from datetime import datetime
# import network

import machine
from machine import Pin

currentTime = datetime.now()
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
Led = Pin(25, Pin.OUT)
Level0 = Pin(12, Pin.IN)
Level1 = Pin(13, Pin.IN)
Level2 = Pin(14, Pin.IN)
Level3 = Pin(15, Pin.IN)
numSensor = 4
count = 0
WaterLevel = [Level0, Level1, Level2, Level3]
print(WaterLevel)
logging.debug(WaterLevel)
print("Github setup complete")

# Define the connection to the Wi-Fi
# def connect():


def counter_function():
    global count
    count = count + 1


def analysis():
    if Level0 == 0 and Level1 == 0 and Level2 == 0 and Level3 == 0:
        print("Water level is 0")
        logging.info("Water level is 0")
    elif Level0 == 1 and Level1 == 0 and Level2 == 0 and Level3 == 0:
        print("Water level is 1")


while True:
    # Trying out the LED onboard
    Led(1)
    print("LED on")
    time.sleep(1)
    Led(0)
    print("LED off")
    time.sleep(0)

    # Doing the analysis
    analysis()
    counter_function()
    print(count)
    time.sleep(1)
    analysis()
    analysis()
    machine.deepsleep(300)
