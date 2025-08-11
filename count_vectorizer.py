
def build_vocab(data):
    data = data.split(" ")
    unique_words = set()
    vocab = {}

    for word in data:
        unique_words.add(word)

    for index, word in enumerate(sorted(list(unique_words))):
        vocab[word] = index
    
    return vocab


def freq_count(data):

    data = data.split(' ')
    data_count = dict.fromkeys(data,0)

    for i in data:
        data_count[i]+=1
    
    return data_count


def vectorize_perfume(notes_string, vocab):
    freq = freq_count(notes_string)
    vector = []
    for word in sorted(vocab.keys()):
        vector.append(freq.get(word,0))
    return vector