from csv import DictReader
import csv

def change_gender(gender):
    gender = gender.split(" ")
    if 'women' in gender and 'men' in gender:
        return "unisex"
    elif 'women' in gender:
        return 'female'
    elif "men" in gender:
        return 'male'
            
header = ["Name", "Gender","Main Accords", "Description"]

output_file = 'clean_data.csv'
input_file = 'fra_perfumes.csv'

with open(output_file, 'a', newline='') as outfile:
    with open(input_file, 'r') as infile:

        writer = csv.writer(outfile)
        if outfile.tell()== 0:
            writer.writerow(header)
        reader = csv.reader(infile)
        header = next(reader)

        for row in reader:
            if row[4] == '[]':
               continue
            row_one = change_gender(row[1])
            new_row = [row[0], row_one, row[4], row[6]]
            writer.writerow(new_row)
        

print(f"CSV file {output_file} created")




# with open('fra_perfumes.csv', 'r') as file:
#     dict_reader = DictReader(file)
    
#     list_of_dicts = list(dict_reader)

# print(list_of_dicts[0])
    