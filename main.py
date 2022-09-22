# Automatic plant watering
import time
from machine import Pin
Led = Pin(25, Pin.OUT)
Level0 = Pin(12, Pin.IN)
Level1 = Pin(13, Pin.IN)
Level2 = Pin(14, Pin.IN)
Level3 = Pin(15, Pin.IN)
numSensor = 4
count = 0
WaterLevel = [Level0, Level1, Level2, Level3]
print(WaterLevel)
print("Github setup complete")



def counter_function():
    global count
    count = count + 1


def analysis():
    if Level0 == 0 and Level1 == 0 and Level2 == 0 and Level3 == 0:
        print("Water level is 0")
    elif Level0 == 1 and Level1 == 0 and Level2 == 0 and Level3 == 0:
        print("Water level is 1")


while True:
    Led(1)
    print("LED on")
    time.sleep(1)
    Led(0)
    print("LED off")
    time.sleep(1)

    analysis()
    counter_function()
    print(count)
    time.sleep(1)
