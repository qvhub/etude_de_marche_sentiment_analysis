# Preparing input ⇒ CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
count_vectorize = CountVectorizer()
count_data = count_vectorize.fit_transform(df['event'].apply(lambda x: ' '.join(x)))

# LDA with sklearn
from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=5,random_state=0)
lda.fit(count_data)
lda.transform(count_data[-2:])

def print_topics(model, count_vectorizer, n_top_words):
    
    '''
    Cette fonction permet de visualiser les mots qui constituent chaque topic
    '''
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    return     