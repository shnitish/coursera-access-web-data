import urllib.request
import simplejson 


url = input('Enter location: ')
print('Retrieving ', url)

data = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved ', str(len(data)) + ' characters')

info = simplejson.loads(data)
sum = 0
total = 0

for comment in info["comments"]:
  sum += int(comment["count"])
  total += 1

print('Count: ', total)
print('Sum: ', sum)
    