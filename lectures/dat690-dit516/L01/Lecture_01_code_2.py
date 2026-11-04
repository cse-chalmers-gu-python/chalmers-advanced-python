'''
Packing of multiple lines in a single variable 
note how this works, also see Q3/Q4 for more packing examples 
'''

with open('./nobel.csv', 'r', encoding='utf-8') as in_file:
    header, *data = in_file.readlines()     # data packing 

nobel_list = []

# fields = header.split(',')

# for i in range(len(fields)):
#     print(fields[i])

# See how this dictionary creation is working / not working 

for line in data:
    temp = {}
    fields = header.split(',')
    values = line.split(',')

    for i in range(len(fields )):
        temp[fields[i]] = values[i]
    nobel_list.append(temp)

for person in nobel_list:
    print(person)
    # input()
