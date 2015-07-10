# coding=UTF-8

# @brief geolocation retrieval for IP addresss
#
# @author webofthink@snu.ac.kr
#

# code snippet from http://stackoverflow.com/questions/9481419/how-can-i-get-the-public-ip-using-python2-7
def get_public_ip():
    from urllib2 import urlopen
    my_ip = urlopen('http://ip.42.pl/raw').read()
    return my_ip

# code snippet from http://stackoverflow.com/questions/2543018/what-python-libraries-can-tell-me-approximate-location-and-time-zone-given-an-ip
def get_geolocation(ip):
    import requests
    FREEGEOPIP_URL = 'http://freegeoip.net/json/'
    url = '{}/{}'.format(FREEGEOPIP_URL, ip)
    print 'send request: ' + url
    response = requests.get(url)
    response.raise_for_status()

    return response.json()