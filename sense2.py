import time
from sense_hat import SenseHat
from beebotte import *

bbt = BBT("jN7s2JnRPkfBMnTDfiGm6xid", "Adc2tynh00GEW8dbodtzRYinisxLNheM")
period = 1
temp_resource = Resource(bbt, "RaspberryPi", "temperature")
humid_resource = Resource(bbt, "RaspberryPi", "humidity")
sense = SenseHat()

sense.clear()


hum = sense.get_humidity()
temp = sense.get_temperature()
# gyro=
temperature = round(temp, 1)
humidity = round(hum, 1)


def getPara():
    temperature = round(temp, 1)
    humidity = round(hum, 1)


print("tempertaure=", temperature)
print("humididity=", humidity)

sense.show_message("temperature: {str(temp)} humidity: {str(humidity)}")


# while(1):
# getPara()
def run():
    while True:
        hum = sense.get_humidity()
        temp = sense.get_temperature()
        temperature = round(temp, 1)
        humidity = round(hum, 1)
        if humidity is not None and temperature is not None:
            print(temperature)
            print(humidity)
            try:
                # Send temperature to Beebotte
                temp_resource.write(temperature)
                # Send humidity to Beebotte
                humid_resource.write(humidity)
            except Exception:
                ## Process exception here
                print("Error while writing to Beebotte")
        else:
            print("Failed to get reading. Try again!")
        time.sleep(period)


run()
