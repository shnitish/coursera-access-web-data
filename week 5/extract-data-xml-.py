import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving: ', url)

data = urllib.request.urlopen(url).read()
print('Retrieved: '+ str(len(data))+ ' characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count: ' + str(len(counts)))

total = 0 
for count in counts:
    total += int(count.text)

print('Sum: '+ str(total))
