# live coding 2025-11-06


## from lecture01/nobel.py

import csv
import json

CSVDATAFILE = '../lecture01/nobel.csv'

with open(CSVDATAFILE, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    tbl = [row for row in csvreader]

yd = {}
for row in tbl[1:]:
  year = int(row[5][:4])
  country = row[10]
  if country == "Sweden":
    if year not in yd: yd[year] = 0
    yd[year] += 1

# print(yd)

# print(tbl[0])
# print(tbl[1])

## end lecture01

data = [{
    'name': row[1],
    'gender': row[2],
    'prize': row[4],
    'year': int(row[5][:4]),
    'birth': int(row[6][:4]),
    'death': row[-1],
    'country': row[-2]
     }
          for row in tbl[1:]]

#for row in data:
#    print(row)


# when we have the json file
JSONDATAFILE = 'nobel.json'

with open(JSONDATAFILE, newline='') as jsonfile:
    data = json.load(jsonfile)

swedes = [row for row in data if row['country'] == 'Sweden']
swedeyears = {row['year'] for row in swedes}
swedegenders = set([row['gender'] for row in swedes])  # not so good as {...}

swedeyearstats = {year: len([sw for sw in swedes if sw['year'] == year])
                  for year in swedeyears}

maxyear = max({year for year in swedeyearstats},
              key=lambda y: swedeyearstats[y])

query = maxyear

print(query)

# the first time
# print(json.dumps(data, indent=2))


