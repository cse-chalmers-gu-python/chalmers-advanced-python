import csv

DATAFILE = '../lecture01/nobel.csv'

with open(DATAFILE, newline='') as file:
    data = [line for line in csv.reader(file, delimiter=',')]

data = data[1:]

data = [{
    'name': row[1],
    'gender': row[2],
    'prize': row[4],
    'year': int(row[5][:4]),
    'birth': int(row[6][:4]),
    'death': row[-1],
    'country': row[-2]
     }
          for row in data]


def age(winner):
    return winner['year'] - winner['birth']

query0 = [(row['name'], age(row)) for row in data
            if row['prize'] == 'Nobel Prize in Physics'
               ]
query1 = set([row['country'] for row in data])
countries = {row['country'] for row in data}

query = {country: len([row for row
                       in data if row['country'] == country])
         for country in countries}

count = len(query)

#for item in query:
#    print(item)

#print(query)

#print(len(query))

#youngest = min(query, key = lambda na: na[1])
    
#print(youngest)

        

import json

# print(json.dumps(data, indent=2))

with open('mynobel.json') as file:
    mydata = json.load(file)

print(mydata[8])




