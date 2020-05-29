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
count = int(input('Enter count: '))
posi = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("Retreiving: ", url)

tag = soup('a')
sequence = []

for i in range(count):
	link = tag[posi - 1].get('href', None)
	print("Retreiving", link)
	sequence.append(tag[posi - 1].contents[0])
	html = urllib.request.urlopen(link,context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tag = soup('a')
	link = tag[posi].get('href', None)

print(sequence[-1])
	