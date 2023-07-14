import json
import urllib.request, urllib.parse, urllib.error

servoiceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#we will do like we did in Urllib1 and 2.
while True :
    address = input('Enter location: ') # we write :  Ann Arbor, MI
    if len(address) < 1: break

    url = servoiceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving' , url)
    urlfile = urllib.request.urlopen(url)
    data = urlfile.read().decode()
    print('Retrieved ', len(data), 'Characters')

    try :
        js= json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to retrieve')
        print(data)
        continue

    print(json.dumps(js, indent = 4)) # the opposite of loads, it return an array with 4 spaces between columns.

    lat  = js["resulsts"][0]["geometry"]["location"]["lat"] # reuslts out of dictionary we start form geometry, this line will result in one line.
    lng  = js["resulsts"][0]["geometry"]["location"]["lng"] #this result in  one line like previouse command.

    print('lat', lat, 'lng', lng)
    location  = js["resulsts"][0]['formatted_address']
    print('location', location)
#this information will not be written cause we must use an API key to access this data.