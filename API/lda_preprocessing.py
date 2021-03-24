import pandas as pd

def remove_word(text):
    remove_word = ["avis", "très", "bon", "restaurant", "banque", "bien", "bonne", "plus", "très", "trop", "super", "jai", "tout", "si", "c", "a"]

    txt = [i for i in text if not i in remove_word]

    return txt

def lda_preprocessing(data):
    data['reviews_processed'] = data['reviews_processed'].apply(lambda x: remove_word(x))

    return data