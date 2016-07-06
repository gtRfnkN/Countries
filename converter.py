import json, urllib2

# get country data
json_data = json.load(urllib2.urlopen('https://raw.githubusercontent.com/gtRfnkN/Countries/master/countries.json'))

# loop through data and store phone, native name and country code by country name
obj = {}
for code, data in json_data["countries"].iteritems():
    for p in data["phone"].split(','):
        obj[data["name"]+p] = {'name': data["name"], 'phone': p, 'native': data["native"], 'code': code, 'weight': '1'}

# write it to a file
with open('countrylist.json', 'w') as outfile:
    json.dump(obj, outfile, sort_keys=True)
