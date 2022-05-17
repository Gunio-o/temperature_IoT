import board
import time
import adafruit_dht
import urllib.request

myAPI = "U4LWQQEXG5HUCL4U"
delay = 600

dhtDevice = adafruit_dht.DHT11(board.D4)

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
print(baseURL)

while True:
	try:
		temperature = dhtDevice.temperature
		humidity = dhtDevice.humidity
		print(
			"Temp: {:.1f}  C    Humidity: {}% ".format(
			temperature, humidity
			)
		)

		print(baseURL + "&field1=%s&field2=%s" % (temperature, humidity))
		webUrl = urllib.request.urlopen(baseURL + "&field1=%s&field2=%s" % (temperature, humidity))
		print(webUrl.read())
		webUrl.close()

	except RuntimeError as error:
		print(error.args[0])
		time.sleep(2.0)
		continue
	except Exception as error:
		dhtDevice.exit()
		raise error

	time.sleep(delay)
