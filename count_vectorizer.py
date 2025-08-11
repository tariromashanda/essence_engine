data = "citrus musky woody aromatic warm spicy lavender mossy fruity earthy white floral lemon mandarin orange cardamom pink pepper lavender green apple orange blossom rose musk moss cedar patchouli"
#data = "doubt thou the stars are fire doubt that the sun doth move doubt truth to be a liar but never doubt i love"
#gets the index of the word
def build_vocab(data):
    data = data.split(" ")
    unique_words = set()
    vocab = {}

    for word in data:
        unique_words.add(word)

    for index, word in enumerate(sorted(list(unique_words))):
        vocab[word] = index
    
    return vocab


#counting the value of each word in a sentence
def freq_count(data):

    data = data.split(' ')
    data_count = dict.fromkeys(data,0)

    for i in data:
        data_count[i]+=1
    
    return data_count

def build_sparse_matrix(vocab,freq):
    vector = []
    for word in vocab:

        vector.append((0, vocab.get(word), freq.get(word)))
    
    return vector

    
def build_bag_of_words(perfume_dict):

    olfactory_notes = ""

    for perfume in perfume_dict:
        olfactory_notes += perfume.get('Olfactory Family Notes')
    
    return olfactory_notes


vocab = build_vocab(data)

freq = freq_count(data)

    
