from network import WLAN
import machine
 
def connect():
    ssid = "XXXXXXXXX"
    password = "XXXXXXXXX"

    wlan = WLAN(mode=WLAN.STA)

    if wlan.isconnected() == True:
        print("Already connected")
        return

    wlan.connect(ssid, auth=(WLAN.WPA2, password), timeout=5000)

    while not wlan.isconnected():
        machine.idle()

    print("Connection successful")
    ip = wlan.ifconfig()
    return ip[0]
