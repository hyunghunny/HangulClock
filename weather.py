# coding=UTF-8

# @brief {brief description]
#
# @author webofthink@snu.ac.kr
#

OWM_API_KEY = 'a7e43d28c0590c1964817fb851a5e42d'
import pyowm
owm = pyowm.OWM(OWM_API_KEY)

observation = owm.weather_at_place('Suwon,kr')
w = observation.get_weather()

print w.get_status()
print w.get_detailed_status()
print w.get_wind()
print w.get_humidity()              # 87
print w.get_temperature('celsius')

from geolocation import get_public_ip
from geolocation import get_geolocation


# get weather information by IP address
my_ip = get_public_ip()
print my_ip

geo_info = get_geolocation(my_ip)
print geo_info

observation_list = owm.weather_around_coords(geo_info['latitude'], geo_info['longitude'])
print len(observation_list)

# XXX: avoid encoding error (see http://libsora.so/posts/python-hangul/)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for observation in observation_list :
    w = observation.get_weather()
    location = observation.get_location()
    print str(unicode(location['name'])) + ": " + w.get_detailed_status()