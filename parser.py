import json
import requests

def hex2ipv4(ip):
    ipv4 = ""
    count = 0
    while count < 4:
        x = int((ip[count] + ip[count + 1]),16)

        if count == 0:
            ipv4 = str(x)
        else:
            ipv4 = ipv4 + "." + str(x)
        count = count + 1
    return ipv4

with open('./20200304123241-bundle.json', encoding="utf-8") as f:
#with open('./20200304124505-bundle.json', encoding="utf-8") as f: 
    data = json.load(f)

hex_ipv6 = []
hex_ipv4 = []
str_ipv4 = []

for key in data:
    ip = data[key]['ip']
    if ip[25:29] == 'ffff':
        hex_ipv4.append(ip[30:33] + ip[35:])
    else:
        hex_ipv6.append(ip)

for ip in hex_ipv4:
    str_ipv4.append(hex2ipv4(ip))

f = open("ipv4.txt",'w', encoding="utf-8")
f.write('ip,country,city,longitude,latitude' + "\n")

for ip in str_ipv4:
    r = requests.get('http://api.ipapi.com/'+ip+'?access_key=90981d6fc04fb91e283346a515cb660b')
    x = r.json()
    country = str(x['country_name'])
    city = str(x['city'])
    longitude = str(x['longitude'])
    latitude = str(x['latitude'])
    if city is not None:
        pass
    else:
        city = ''
    if longitude is not None:
        pass
    else:
        longitude = ''
    if latitude is not None:
        pass
    else:
        latitude = ''
        
    f.write(str(ip) + ',' + str(country) + ',' + str(city) + ',' + str(longitude) + ',' + str(latitude) + "\n")

