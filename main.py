from data_cleaner import csv_to_list_of_dicts
from count_vectorizer import build_vocab, vectorize_perfume
from perfume_recommendation import recommend_perfumes



def main():

    perfume_name = input("Please enter perfume ")

    perfume_list = csv_to_list_of_dicts('clean_perfume_data.csv')

    all_notes = " ".join([p['Olfactory Family Notes'] for p in perfume_list])
    vocab = build_vocab(all_notes)

    perfume_vectors = []

    for p in perfume_list:
        perfume_vectors.append(vectorize_perfume(p['Olfactory Family Notes'], vocab))
    
    recs = recommend_perfumes(perfume_name, perfume_list, perfume_vectors, top_n=3)
    
    for name, score in recs:
        print(f"{name}: {score}")


if __name__ == "__main__":
    main()