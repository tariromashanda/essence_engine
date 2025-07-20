from csv import DictReader
import csv

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
          new_row = [row[0], row[1], row[4], row[6]]
          writer.writerow(new_row)
        

print(f"CSV file {output_file} created")


# with open('fra_perfumes.csv', 'r') as file:
#     dict_reader = DictReader(file)
    
#     list_of_dicts = list(dict_reader)

# print(list_of_dicts[0])
    