from csv import DictReader

with open('fra_perfumes.csv', 'r') as file:
    dict_reader = DictReader(file)
    
    list_of_dict = list(dict_reader)

print(list_of_dict[1])
    