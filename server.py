# Automatic plant watering
# TOOL -> MicroPython -> MicroPython REPL
# STRG D löst soft rest aus | STRG C für programm cancel | STRG ] für
# Local wieder schließen um Microcontroller flashen zu können
# Bibliotheken laden
import machine
import network
import socket
import rp2
import utime as time
from machine import Pin

# WLAN-Konfiguration
wlanSSID = 'LAN solo'
wlanPW = 'IQ7Fz4K%L&zL5'
rp2.country('DE')

# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)
# Initialisierung von GPIO17 als Eingang mit internem PULLUP-Widerstand (Taster S1)
Level0 = Pin(17, Pin.IN, Pin.PULL_UP)
# Initialisierung von GPIO16 als Eingang mit externem PULLUP-Widerstand (Taster S2)
Level1 = Pin(16, Pin.IN)
# Initialisierung von GPIO14 als Eingang mit internem PULLDOWN-Widerstand (Taster S3)
Level2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
# Initialisierung von GPIO15 als Eingang mit externem PULLDOWN-Widerstand (Taster S4)
Level3 = Pin(15, Pin.IN)

# Logging for better debugging
currentTime = time.gmtime()
# print(currentTime)
# logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

numSensor = 4
count = 0
WaterLevel = [Level0, Level1, Level2, Level3]
# print(WaterLevel)
# logging.debug(WaterLevel)


# Funktion: WLAN-Verbindung
def wlan_connect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen')
        wlan.active(True)
        wlan.connect(wlanSSID, wlanPW)
        for i in range(10):
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            led_onboard.toggle()
            print('.', wlan.status())
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt')
        led_onboard.on()
        print('WLAN-Status:', wlan.status())
        netConfig = wlan.ifconfig()
        ip = netConfig[0]
        print('IPv4-Adresse:', netConfig[0], '/', netConfig[1])
        print('Standard-Gateway:', netConfig[2])
        print('DNS-Server:', netConfig[3])
    else:
        print('Keine WLAN-Verbindung')
        led_onboard.off()
        print('WLAN-Status:', wlan.status())
    return ip


def open_socket(ip):
    address = (ip, 80)
    #address = socket.getaddrinfo('0,0,0,0', 80)[0][-1]
    s = socket.socket()
    s.bind(address)
    s.listen(1)
    print("Listening on ", address)

    # Start a web server
    status = analysis()
    while True:
        try:
            client, addr = s.accept()
            print('client connected from', addr)
            request = client.recv(1024)
            print("request:")
            request = str(request)
            print("Trying to perform webpage")
            html = webpage(status)
            client.send(html)
            client.close()
            print("Serve done")
        except OSError as e:
            client.close()
            print('connection closed')

def webpage(status):
    # Template HTML
    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Overview automated watering system</title>
<meta http-equiv="refresh" content="10">
<meta http-equiv="refresh" content="10">
</head>
<body>
<table>
    <tr>
        <th>Pflanze:</th>
        <th>Wasser:</th>
        <th>Sonne:</th>
    <tr>
    <tr>
        <td>Bananenstaude</td>
        <td>Low</td>
        <td>2</td>
    <tr>
    <tr>
        <td>Geigenbaum</td>
        <td>Low</td>
        <td>2</td>
    <tr>
    <tr>
        <td>Efeutute</td>
        <td>Low</td>
        <td>2</td>
    <tr>
    <tr>
        <td>Pfannkuchenpflanze</td>
        <td>Low</td>
        <td>2</td>
    <tr>
    <tr>
        <td>Blume</td>
        <td>Low</td>
        <td>2</td>
    <tr>
</table>
</body>
</html>
"""
    print("Webpage configurated")
    return str(html)


def counter_function():
    global count
    count = count + 1


def analysis():
    if Level0.value() == 0 and Level1.value() == 0 and Level2.value() == 0 and Level3.value() == 0:
        led_onboard.on()
        status = "Water empty"
        # logging.info("Water level is 0")
    elif Level0.value() == 1 and Level1.value() == 0 and Level2.value() == 0 and Level3.value() == 0:
        led_onboard.on()
        status = "Water level low"

    print("Analysis done:", status)
    return status


# WLAN-Verbindung herstellen
try:
    ip = wlan_connect()
    open_socket(ip)
    print("Data loaded to something")
except KeyboardInterrupt:
    machine.reset()


