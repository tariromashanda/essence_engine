from data_cleaner import csv_to_list_of_dicts
from count_vectorizer import build_vocab, freq_count

perfume_list = csv_to_list_of_dicts("clean_perfume_data.csv")

all_notes = " ".join([p['Olfactory Family Notes'] for p in perfume_list])
voab = build_vocab(all_notes)