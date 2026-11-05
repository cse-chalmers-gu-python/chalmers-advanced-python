'''
1 - Reading CSV file in POPO
2 - building query functions 
'''

import csv
CSV_FILE = './nobel.csv'

def build_noble_data(csvfile):
    nobel_data = []     # This is Plain-Old-Python-Object (POPO)

    with open(csvfile, 'r', encoding='utf-8', newline='') as csv_input:
        csv_obj = csv.reader(csv_input, delimiter=',', quotechar='"' )
        header = next(csv_obj)
        for row in csv_obj:
            nobel_data.append(
                {
                    'name': row[1],
                    'sex': row[2],
                    'award': row[4],
                    'date': row[5][:10],
                    'time': row[5][11:-1],
                    'country': row[10]
                }
            )
    return nobel_data

nobel_list = build_noble_data(CSV_FILE)

# for person in nobel_list:
#     print(person['name'], person['country'])
#     input()

def test_data_building(data_building_function, args):
    '''
    This function tests if our nobel_list is created correctly or not 
    '''
    nobel_list = data_building_function(args)

    assert isinstance(nobel_list, list), "nobel list must be a list of dictionaries, which it seems not to be"

    assert nobel_list, "Nobel List shall contain at least one person's record"

    expected_headers = { 'name', 'sex', 'award', 'date', 'time', 'country'}

    assert set(nobel_list[0]) == expected_headers, "Expected headers are not present in our data"

test_data_building(build_noble_data, CSV_FILE)

def query_nobel_data(nobel_list, name):
    '''
    Query nobel_list to find information of interest
    '''
    # Filtering data 
    swedish_nobels = [ person['name'] for person in nobel_list 
                      if person['country'] == 'Sweden']
    # return swedish_nobels

    # Filtering 
    countries = { person['country'] for person in nobel_list }
    # return countries 

    # Searching
     
    # hits = [ person for person in nobel_list
    #         if name.lower() in person['name'].lower() ]


    # We can either use selection function, or we can use lambda function as in hits
    def selection(person):
        if name.lower() in person['name'].lower():
            return True
        else: 
            return False 

    hits2 = filter(selection, nobel_list)

    hits = filter(
        lambda person: name.lower() in person['name'].lower(), nobel_list )

    return hits2

query_results = query_nobel_data(nobel_list, 'Bragg')
print(list(query_results))