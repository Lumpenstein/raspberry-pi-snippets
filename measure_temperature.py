import os
import time

def measure_temperature():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        print(measure_temperature())
        time.sleep(1)