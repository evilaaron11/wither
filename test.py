import requests
API_KEY = "b525cc3cbc2614ce4eb29539179bb821"
ipdata = requests.get("http://ipinfo.io")
ipdata = ipdata.json()
#print ipdata['postal']
api_url = "http://api.openweathermap.org/data/2.5/weather?zip=" + \
            str(ipdata['postal']) + "," + ipdata['country'] + "&APPID=" \
            + API_KEY + "&units=imperial"
print api_url
r = requests.get(api_url)

print r.status_code
if r.status_code != requests.codes.ok:
   print "Invalid location"
   quit()

elem = r.json()

print str(elem['main']['temp']) + " Degrees F"
print "High of " + str(elem['main']['temp_max']) + " Degrees F"
#print r
