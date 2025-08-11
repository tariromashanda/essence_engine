from cosine_similarity import cosine_similarity

def recommend_perfumes(target_name, perfume_list, perfume_vetcors, top_n = 5):
    target_index = next((i for i, p in enumerate(perfume_list) if p['Name'] == target_name), None)

    if target_index is None:
        return []
    
    target_vector = perfume_vetcors[target_index]
    similarities = []

    for i, vec in enumerate(perfume_vetcors):
        if i == target_index:
            continue
        sim = cosine_similarity(target_vector, vec)
        similarities.append((perfume_list[i]['Name'], sim))
    
    similarities.sort(key = lambda x: x[1], reverse = True)
    
    return similarities[:top_n]

