import csv

dataset = open('worldcities.csv')
reader = csv.reader(dataset, delimiter=',')
first = True

cities = []

for row in reader:
    if first:
        first = False
        continue

    cities.append(row[1].replace('"', ''))

f = open('cities', 'w')
for city in cities:
    f.write(city + '\n')
f.close()
