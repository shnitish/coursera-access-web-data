import re 

x = []

with open('samplefile.txt') as file:
	for line in file:
		y = re.findall('[0-9]+', line)
		x += y
		
sum = 0

for string in x:
 	sum += int(string)

print(sum)
