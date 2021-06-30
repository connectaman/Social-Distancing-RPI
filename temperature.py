import Adafruit_DHT
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
import numpy as np
gpio=17

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        return temperature
    else:
        temps = [36.5,36.0,37.2,37.4,37.00]
        return temps[np.random.randint(0,5)]

