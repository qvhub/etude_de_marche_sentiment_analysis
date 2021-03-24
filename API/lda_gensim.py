# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import pandas as pd
import json



def dictionary_corpus_ldamodel(texts, numbers_topics):
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
        
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=numbers_topics, id2word = dictionary, passes=20)

    result = ldamodel.show_topics(num_topics=numbers_topics, num_words=10, log=False, formatted=True)

    return result

def lda_gensim_topics(data, numbers_topics):

    # Creat 2 dataFrame data_pos and data_neg
    data_pos = data.loc[data['sentiment'] == 1]
    data_neg = data.loc[data['sentiment'] == 0]

    # Creat texts from dataFrame
    #texts_pos = data_pos['reviews_processed']
    #texts_neg = data_neg['reviews_processed']

    print(data_pos)
    print('\n')
    print(data_neg)
    print('\n')
    
    result_pos = dictionary_corpus_ldamodel(data_pos['reviews_processed'], numbers_topics)
    result_neg = dictionary_corpus_ldamodel(data_neg['reviews_processed'], numbers_topics)

    print('-------------------------------------------------------------------------------------------')
    print(result_pos)
    print('-------------------------------------------------------------------------------------------')
    print(result_neg)
    print('-------------------------------------------------------------------------------------------')

    #result_pos = json.dumps(result_pos)
    #result_neg = json.dumps(result_neg)

    return result_pos, result_neg










