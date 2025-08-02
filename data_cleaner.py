import csv
import re

def change_gender(gender):
    gender = gender.split(" ")
    if 'women' in gender and 'men' in gender:
        return "unisex"
    elif 'women' in gender:
        return 'female'
    elif "men" in gender:
        return 'male'
            
def change_name(name):
    pattern_one = "for women and men"
    pattern_two = "for men"
    pattern_three = "for women"

    match_one = re.search(pattern_one, name)
    match_two = re.search(pattern_two, name)
    match_three = re.search(pattern_three, name)

    if match_one:
        new_name = re.sub(pattern_one, "", name)
    elif match_two:
        new_name = re.sub(pattern_two, "", name)
    elif match_three:
        new_name = name = re.sub(pattern_three, "", name)
    return new_name

def remove_stop_words(notes):

    notes = re.sub(r'[^\w\s]', '', notes)

    stop_words = ["top", "notes", "are","middle", "base", "and", "is", "note"]
    notes = notes.split()

    clean_notes = [word for word in notes if word.lower() not in stop_words]
    result = " ".join(clean_notes)


    pattern_one = ","
    pattern_two = ";"

    match_one = re.search(pattern_one, result)

    if match_one:
        result = re.sub(pattern_one, "", result)
    
    match_two = re.search(pattern_two, result)
    
    if match_two:
        result = re.sub(pattern_two, "", result)

    return result

def change_notes(notes):
    notes = notes.lower()
    pattern_top_notes = r"top note.*?;"
    pattern_middle_notes = r"middle note.*?;"
    pattern_base_notes = r"base note.*?[?.!]$"

    match_top_notes = re.search(pattern_top_notes, notes)
    match_middle_notes = re.search(pattern_middle_notes, notes)
    match_base_notes = re.search(pattern_base_notes, notes)

    notes = []

    if match_top_notes:
        top_notes = match_top_notes.group()
        top_notes_clean = remove_stop_words(top_notes)
        notes.append(top_notes_clean)
    else:
        notes.append(0)

    if match_middle_notes:
        middle_notes = match_middle_notes.group()
        middle_notes_clean = remove_stop_words(middle_notes)
        notes.append(middle_notes_clean)
    else:
        notes.append(0)

    if match_base_notes:
        base_notes = match_base_notes.group()
        base_notes_clean = remove_stop_words(base_notes)
        notes.append(base_notes_clean)
    else:
        notes.append(0)
    
    return notes

def change_main_accord(accord):

    accord = re.sub(r"['\"\[\],]" , "", accord)

    return accord


def clean_file(input_file):

    header = ["Index", "Name", "Gender","Olfactory Family Notes"]
    output_file = 'clean_perfume_data.csv'

    with open(output_file, 'a', newline='') as outfile:
        with open(input_file, 'r') as infile:

            writer = csv.writer(outfile)

            index = 0

            if outfile.tell()== 0:
                writer.writerow(header)

            reader = csv.reader(infile)
            header = next(reader)

            for row in reader:
                if row[4] == '[]':
                    continue
                name = change_name(row[0])
                gender = change_gender(row[1])
                notes = change_notes(row[6])
                accords = change_main_accord(row[4])
                index +=1

                if 0 in notes:
                    continue
                new_row = [index, name, gender, create_soup(accords, notes)]
                writer.writerow(new_row)
            

    print(f"CSV file {output_file} created")

def create_soup(row_one, row_two):

    row_two =", ".join(row_two).replace(",","")

    return row_one+" "+row_two

# def get_perfume_index(file, name):

#     with open(file, newline = '') as file:
#         reader = csv.reader(file)
#         next(reader, None)
#         for row in reader:
#             if row[1] == name:
#                 return row[0]


def csv_to_list_of_dicts(filepath):
    data = []

    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header row
        for row in reader:
            row_dict = {
                'Index': row[0],
                'Name': row[1],
                'Gender': row[2],
                'Olfactory Family Notes': row[3]
            }
            data.append(row_dict)

    return data

def build_reverse_mapping(perfume_list):
    mapping = {}
    for i, perfume in enumerate(perfume_list):
        mapping[perfume['Name']] = i
    return mapping

dict1 = csv_to_list_of_dicts("clean_perfume_data.csv")
