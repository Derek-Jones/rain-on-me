#
# raininme-serv.py, 18 Oct 14
#

from json import loads
from urllib2 import urlopen
from datetime import datetime, date, timedelta

def download_json(url):
   weather = urlopen(url)
   string = weather.read()
   weather.close()
   return loads(string)

date_time=date.today()

# Not our actual key, don't want that to appear on github
our_key='485014baf636a61b'

# Current location
# The client passes us current lat/long, hard code TechCrunch dungeon location for now
cur_lat=51.508907
cur_long=-0.084054

# Get list of weather stations around us
# Example from wunderground doc
# http://api.wunderground.com/api/485014baf636a61b/geolookup/q/37.776289,-122.395234.json

loc_station_url=''.join(['http://api.wunderground.com/api/', our_key, '/geolookup/q/', str(cur_lat), ',', str(cur_long), '.json'])

# print loc_station_url

station_info=download_json(loc_station_url)
our_locations=station_info['location']

# Now we have either 50 locations or all locations within 40km
# But all we know is their distance, not their location
# (do wunderground want people to use up their API call budget so they make more money?)


# http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KCASANTE9&graphspan=month&month=10&day=1&year=2012&format=1



d,x,y=[],[],[]
x1 = 0.0
key = 'Your key here'
for day in range(4,-1,-1):
   url = ''.join(['http://api.wunderground.com/api/', our_key, '/history_', (now-timedelta(days=day)).strftime('%Y%m%d'), '/q/TX/Addison.json'])
   data = download_json(url)
for k in data['history']['observations']:
   y0 = float(k['pressurem'])
   if y0 < 0.0:
      continue
   else:
      x.append(x1 + float(k['date']['hour'])+ round((float(k['date']['min'])/60.0),2))
   y.append(y0)
x1 += 24.0

