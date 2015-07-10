# coding=UTF-8

# @brief weather information retrieval
#
# @author webofthink@snu.ac.kr
#

OWM_API_KEY = 'a7e43d28c0590c1964817fb851a5e42d'
import pyowm
owm = pyowm.OWM(OWM_API_KEY)

def printSuwonWeather() :
    # get suwon weather info
    observation = owm.weather_at_place('Suwon,kr')
    w = observation.get_weather()

    print w.get_status()
    print w.get_detailed_status()
    print w.get_wind()
    print w.get_humidity()              # 87
    print w.get_temperature('celsius')

def getKoreaWeather(location):
    location = location + ',kr'
    print "get weather info @" + location
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    returnObj = {}
    returnObj['location'] = location
    returnObj['status'] = w.get_status()
    returnObj['wind'] = w.get_wind()
    returnObj['humidity'] = w.get_humidity()              # 87
    returnObj['temperature'] = w.get_temperature('celsius')
    return returnObj

#####################################

def getNearbyWeather() :
    from geolocation import get_public_ip
    from geolocation import get_geolocation

    # get weather information by IP address
    my_ip = get_public_ip()
    print my_ip

    geo_info = get_geolocation(my_ip)
    print "get weather info @" + geo_info['city']

    observation_list = owm.weather_around_coords(geo_info['latitude'], geo_info['longitude'])
    print len(observation_list)

    # XXX: avoid encoding error (see http://libsora.so/posts/python-hangul/)
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    returnList = []
    for observation in observation_list :
        w = observation.get_weather()
        location = observation.get_location()
        returnObj = {}
        returnObj[str(unicode(location.get_name()))] = w.get_detailed_status()
        returnList.append(returnObj)

    return returnList