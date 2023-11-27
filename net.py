import socket
import time
import urllib.request
import json

'''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()


mysock.send(cmd)


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()

'''
'''
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect((HOST, PORT))

mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
'''
'''
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

'''  
'''
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
'''
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('h2')
for tag in tags:
    print(tag)

'''
import urllib.request
import json

apikey = ""
secret = ""

hosturl = "http://ws.audioscrobbler.com"
artist = "Ghostface+Killah"

artist = input("enter an artist")
artist = artist.replace(" ", "+")

queryurl = f"/2.0/?method=artist.getinfo&artist={artist}&api_key={apikey}&format=json"

url = hosturl + queryurl

data = urllib.request.urlopen(url).read()

artistinfo = json.loads(data)

artist = artistinfo["artist"]

print("Name = ", artist["name"])
# print("bio = ", artist["bio"]["summary"])

ontour = int(artist["ontour"])
ontour = bool(ontour)
if ontour:
    print(artist["name"], " is on tour, go get robbed by ticketmaster")
else:
    print(artist["name"], " is probably at home")


'''

latitude = "42.701283"
longitude = "-71.175682"

weatherURL = f"https://api.weather.gov/points/{latitude},{longitude}"

data = urllib.request.urlopen(weatherURL).read()
weather = json.loads(data)
office = weather["properties"]["gridId"]
gridX = weather["properties"]["gridX"]
gridY = weather["properties"]["gridY"]

forecastURL = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
forecastData = urllib.request.urlopen(forecastURL).read()
forecast = json.loads(forecastData)
print(forecastURL)
days = forecast["properties"]["periods"]

print("today",days[0]['detailedForecast'])
print("tonight",days[1]['detailedForecast'])
print("tomorrow",days[2]['detailedForecast'])
print("tomorrw night",days[3]['detailedForecast'])
'''