#!/usr/bin/env python

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

result = pywapi.get_weather_from_yahoo('USAZ0082', 'metric')
pp.pprint(result)