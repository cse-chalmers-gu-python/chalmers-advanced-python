import csv 
import json 

IN_FILE = './nobel.csv'

def read_lines(file):
    with open(file, 'r', encoding='utf-8', newline='') as infile:
        for line in csv.reader(infile, delimiter=',', quotechar='"'):
            yield line

def build_nobel_dict():
    file_gen = read_lines(IN_FILE)
    headers = next(file_gen)

    noble_dict = {   }

    for line in file_gen:
        noble_dict[line[1]] = { 
            'webpage': line[0],
            'sex': line[2],
            'prize': line[4],
            'award_date': line[5],
            'birth_date': line[6],
            'death_date': line[-1]  
        }

    return noble_dict

nobel_dict = json.load()
nobel_dict = build_nobel_dict()

def store_json(nobel_dict, json_file):
    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(nobel_dict, outfile, indent=4)

store_json(nobel_dict, './nobel.json')

print(nobel_dict['Clinton Davisson']['prize'])