#
# raininme-serv.py, 18 Oct 14
#


http://api.wunderground.com/api/485014baf636a61b/geolookup/q/37.776289,-122.395234.json

http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KCASANTE9&graphspan=month&month=10&day=1&year=2012&format=1

from json import loads
from urllib2 import urlopen
from datetime import datetime, timedelta

def download_json(url):
   weather = urlopen(url)
   string = weather.read()
   weather.close()
   return loads(string)

d,x,y=[],[],[]
x1 = 0.0
key = 'Your key here'
for day in range(4,-1,-1):
   url = ''.join(['http://api.wunderground.com/api/', key, '/history_', (now-timedelta(days=day)).strftime('%Y%m%d'), '/q/TX/Addison.json'])
   data = download_json(url)
for k in data['history']['observations']:
   y0 = float(k['pressurem'])
   if y0 < 0.0:
      continue
   else:
      x.append(x1 + float(k['date']['hour'])+ round((float(k['date']['min'])/60.0),2))
   y.append(y0)
x1 += 24.0

