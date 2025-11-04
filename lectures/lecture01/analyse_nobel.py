import csv

DATAFILE = 'nobel.csv'

with open(DATAFILE, newline='') as file:
    data = []
    myreader = csv.reader(file, delimiter=',')
    for line in myreader:
        data.append(line)

titles = data[0]

print(titles)

data = data[1:]

rowlength = len(titles)
print(rowlength)

count = 0
for row in data:
    if row[-2] == 'Sweden':
        print(row[1])
        count += 1

print(count)

        



