import os
from datetime import datetime as DateTime
import time

wanIP = "google.de"
Dateiname = "001_PingWAN.txt"
checkIntervall = 30
i = 0


def CheckPing(ip):
    with open('001_PingWAN.txt', 'a') as datei:
        if os.system("ping -c 1 " + ip) == 0:
            print (DateTime.now().strftime('%Y.%m.%d - %H:%M:%S') + " = WAN " + ip + " erreichbar")
            # datei.write("\r" + (DateTime.now().strftime('%Y.%m.%d - %H:%M:%S') + " = WAN " + ip + " erreichbar"))
        else:
            # print (DateTime.now().strftime('%Y.%m.%d - %H:%M:%S') + " =  !!! WAN " + ip + "NICHT ERREICHBAR !!!")
            datei.write("\r" + (DateTime.now().strftime('%Y.%m.%d - %H:%M:%S') + " =  !!! WAN " + ip + " NICHT ERREICHBAR !!!"))

    datei.close()


try:
    with open('001_PingWAN.txt', 'a') as datei:
        datei.write("\r" + "---- Restart -----")
    datei.close()

    while True:
        CheckPing(wanIP)
        time.sleep(checkIntervall)
        if i == 30:
            with open('001_PingWAN.txt', 'a') as datei:
                datei.write("\r" + (DateTime.now().strftime('%Y.%m.%d - %H:%M:%S') + " =  runing Script"))
            datei.close()
            i = 0
        else:
            i = i + 1

except KeyboardInterrupt:
    pass
