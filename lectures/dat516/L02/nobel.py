"""
Working with Nobel data as a list of lists
"""

# data = [
#   ['person', 'name', 'sex', 'award', 'date', 'birthDate'],
#   ['Q462843', 'Tu Youyou', 'female', 'Nobel Prize in Physiology or Medicine', '2015-01-01', '1930-12-30'],
#   ['Q89620738', 'John Michael Jumper', 'male', 'Nobel Prize in Chemistry', '2024-01-01', '1985-01-01'],
#   ['Q1267', 'Dag Hammarskjöld', 'male', 'Nobel Peace Prize', '1961-01-01', '1905-07-29'],
# ]

# without using csv library:
# data = []
# with open('nobel.csv') as f:
#   for line in f:
#     data.append(line.strip().split(','))

import csv
data = []
with open('nobel.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        data.append(row)

lol = data

# women
count = 0
for row in data[1:]:
  if row[2] == 'female':
    count += 1
print(f'Women: {count}')

# women born after 1970
year = '1970'
count = 0
for row in data[1:]:
  if row[2] == 'female' and row[6][:4] > year:
    count += 1
print(f'Women born after {year}: {count}')

# Swedish winners per year
yd = {}
for row in data[1:]:
  year = int(row[5][:4])
  country = row[10]
  if country == "Sweden":
    if year not in yd: yd[year] = 0
    yd[year] += 1
print(yd)


"""
Using to list of dicts
"""

# data = [
#   {'person': 'http://www.wikidata.org/entity/Q131721', 'personLabel': 'Johannes Diderik van der Waals', 'sexLabel': 'male', 'award': 'http://www.wikidata.org/entity/Q38104', 'awardLabel': 'Nobel Prize in Physics', 'date': '1910-01-01T00:00:00Z', 'birthDate': '1837-11-23T00:00:00Z', 'birthPlace': 'http://www.wikidata.org/entity/Q43631', 'birthPlaceLabel': 'Leiden', 'country': 'http://www.wikidata.org/entity/Q55', 'countryLabel': 'Netherlands', 'deathDate': '1923-03-08T00:00:00Z'},
#   {'person': 'http://www.wikidata.org/entity/Q131729', 'personLabel': 'William Lawrence Bragg', 'sexLabel': 'male', 'award': 'http://www.wikidata.org/entity/Q38104', 'awardLabel': 'Nobel Prize in Physics', 'date': '1915-01-01T00:00:00Z', 'birthDate': '1890-03-31T00:00:00Z', 'birthPlace': 'http://www.wikidata.org/entity/Q5112', 'birthPlaceLabel': 'Adelaide', 'country': 'http://www.wikidata.org/entity/Q408', 'countryLabel': 'Australia', 'deathDate': '1971-07-01T00:00:00Z'}
# ]

with open('nobel.tsv') as f:
  rows = csv.DictReader(f, delimiter='\t')
  data = list(rows)

lod = data

yd = {}
for row in data:
  country = row["countryLabel"]
  year = int(row["date"][:4])
  if country == "Sweden":
    if year not in yd: yd[year] = 0
    yd[year] += 1
print(yd)

# compare sizes
import pysize
print("list of lists:", pysize.get_size(lol), "bytes")
print("list of dicts:", pysize.get_size(lod), "bytes")

"""
Using comprehensions
"""

data = [
  {
    'name': row["personLabel"],
    'gender': row["sexLabel"],
    'prize': row["awardLabel"],
    'year': int(row["date"][:4]),
    'birth': int(row["birthDate"][:4]),
    'death': int(row["deathDate"][:4]) if row["deathDate"] else None,
    'country': row["countryLabel"]
  }
  for row in data
]

# women born after 1970
year = 1970
count = 0
for row in data:
  if row["gender"] == 'female' and row["birth"] > year:
    count += 1
print(f'Women born after {year}: {count}')

# using list comprehensions
women = [ row for row in data if row["gender"] == "female" ]
women_born_after = [ row for row in women if row["birth"] > year ]
print(f'Women born after {year}: {len(women_born_after)}')


def age(winner):
    return winner['year'] - winner['birth']

query0 = [
  (row['name'], age(row)) for row in data
  if row['prize'] == 'Nobel Prize in Physics'
]
query1 = set([row['country'] for row in data])
countries = {row['country'] for row in data}

query = {country: len([row for row
                       in data if row['country'] == country])
         for country in countries}

count = len(query)

"""
Loading from JSON
"""

import json

# Save previous data as JSON
# with open('nobel.json', 'w') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

with open('nobel.json') as file:
    data = json.load(file)

swedes = [row for row in data if row['country'] == 'Sweden']
swedeyears = {row['year'] for row in swedes}
swedegenders = set([row['gender'] for row in swedes])  # not so good as {...}

swedeyearstats = {year: len([sw for sw in swedes if sw['year'] == year])
                  for year in swedeyears}

maxyear = max({year for year in swedeyearstats},
              key=lambda y: swedeyearstats[y])

query = maxyear

print(query)
