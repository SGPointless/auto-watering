import socket
import network
import rp2
import machine
from machine import Pin
import utime as time


# WLAN-Konfiguration
wlanSSID = 'LAN solo'
wlanPW = 'IQ7Fz4K%L&zL5'
rp2.country('DE')

# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)


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


ip = wlan_connect()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, 80))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")