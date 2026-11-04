'''
Multiple ways to read data from a CSV file 
You can use lazy evaluation (file iterator) or you 
can use eager methods to copy the entire file in your memory 
'''

from sys import getsizeof
with open('./nobel.csv', 'r', encoding='utf-8') as in_file: # in_file is a file iterator 
    # header = next(in_file)
    # first_line = next(in_file)
    # second_line = next(in_file)
    # for line in in_file:      # Iterator method is Lazy 
    #     print(line)
    data = in_file.readlines()  # reading entire content of file is eager 

for line in data:
    print(line)

# print(getsizeof(header), type(header), header)
# print(first_line)
# print(second_line)
# with open('./nobel.csv', 'r', encoding='utf-8') as in_file:
#     a = in_file.readlines()
#     b = in_file.read()

# print(type(a), len(a), end='\t')
# print(type(b), len(b))