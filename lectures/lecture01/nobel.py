# tbl = [
#   ['person', 'name', 'sex', 'award', 'date', 'birthDate'],
#   ['Q462843', 'Tu Youyou', 'female', 'Nobel Prize in Physiology or Medicine', '2015-01-01', '1930-12-30'],
#   ['Q89620738', 'John Michael Jumper', 'male', 'Nobel Prize in Chemistry', '2024-01-01', '1985-01-01'],
#   ['Q1267', 'Dag Hammarskjöld', 'male', 'Nobel Peace Prize', '1961-01-01', '1905-07-29'],
# ]

# tbl = []
# with open('nobel.csv') as f:
#   for line in f:
#     tbl.append(line.strip().split(','))

import csv
tbl = []
with open('nobel.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        tbl.append(row)

yd = {}
for row in tbl[1:]:
  year = int(row[5][:4])
  country = row[10]
  if country == "Sweden":
    if year not in yd: yd[year] = 0
    yd[year] += 1

print(yd)
