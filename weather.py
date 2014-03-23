import pywapi
import string
import pprint

pp = pprint.PrettyPrinter(indent=4)
#weather_com_result = pywapi.get_weather_from_weather_com('85296')
yahoo_result = pywapi.get_weather_from_yahoo('USAZ0082', 'imperial')
#noaa_result = pywapi.get_weather_from_noaa('KJFK')

#print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "F now in Arizona.\n\n" + yahoo_result['condition']['date']

pp.pprint(yahoo_result['forecasts'])
#print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York.\n"