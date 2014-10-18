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

def get_cur_location():
# Current location
# The client passes us current lat/long, hard code TechCrunch dungeon location for now
   return [51.508907, -0.084054]


def rain_prediction():

   cur_lat_long=get_cur_location()
   cur_lat=cur_lat_long[0]
   cur_long=cur_lat_long[1]
   date_time=date.today()

# Not our actual key, don't want that to appear on github
   our_key='485014baf636a61b'


# Get list of weather stations around us
# Example from wunderground doc
# http://api.wunderground.com/api/485014baf636a61b/geolookup/q/37.776289,-122.395234.json

   loc_station_url=''.join(['http://api.wunderground.com/api/', our_key, '/geolookup/q/', str(cur_lat), ',', str(cur_long), '.json'])

#   print loc_station_url

# station_info=download_json(loc_station_url)
# our_locations=station_info['location']

# Now we have either 50 locations or all locations within 40km
# But all we know is their distance, not their location
# (do wunderground want people to use up their API call budget so they make more money?)

# Save on our daily limit of API calls by reusing data that is unlikely to change

   london_f = open('../data/london-station.json')
   london_station=london_f.read()

# http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KCASANTE9&graphspan=month&month=10&day=1&year=2012&format=1


#   x,y=[],[]
#
#   data_url = ''.join(['http://api.wunderground.com/api/', our_key, '/history_', date_time.strftime('%Y%m%d'), '/q/TX/Addison.json'])
#   data = download_json(data_url)
#
#   for k in data['history']['observations']:
#      y0 = float(k['pressurem'])
#      if y0 < 0.0:
#         continue
#      else:
#         x.append(x1 + float(k['date']['hour'])+ round((float(k['date']['min'])/60.0),2))
#      y.append(y0)

   rain_f = open('../data/rainonme.json')
   rain_pred=rain_f.read()
   return rain_pred

if __name__ == '__main__':
   t=rain_prediction()
   print t
