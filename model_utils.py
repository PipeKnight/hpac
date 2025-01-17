import codecs
import numpy as np
import random

from collections import Counter


def _read_embedding_file(file_embedding):
    
    if file_embedding is None:
     
        raise ValueError("Path in file_embedding: ", file_embedding," does not exist.")
    with open(file_embedding,'r') as external_embedding_fp:
        line = external_embedding_fp.readline()
        esize = len(line.split()) -1

        pad_element_vector = [0.]*esize
        unk_element_vector = [0.]*esize
        vectors = [pad_element_vector,unk_element_vector]
        iembeddings = {}
      #  line = external_embedding_fp.readline()
        iline = 1
        while line != '': 
            vector = [float(f) for f in line.strip('\n').split(' ')[1:]] 
            word = line.split(' ')[0]
            vectors.append(vector)
            iembeddings[word] = iline
            iline+=1
            line = external_embedding_fp.readline()
    lookup = np.array(vectors)
    return iembeddings, lookup, esize
        


def load_data(path, path_spells, train=True, d_l=None):

    if train:
        d_l = {}
        with codecs.open(path_spells) as f:
            labels = ["_".join(l.strip().upper().split()) for l in f.readlines()]

    words = []
    labels = set([])
    with codecs.open(path) as f:
        l = f.readline()
        while l != '':
            ls = l.split('\t')
            labels.add(ls[1])
            words.extend(iter(ls[2].split()))
            l = f.readline()       

    word_counter = Counter(words)

    return word_counter, labels



