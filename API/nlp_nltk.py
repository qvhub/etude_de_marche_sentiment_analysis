import nltk
import pandas as pd
import numpy as np
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def verification(result, rate_base):
    if result == 1:
        if rate_base > 2.5:
            return 1
        else:
            return 0
    if result == 0: 
        if rate_base < 2.5:
             return 1
        else:
            return 0         


def sentiment_analysis(data):

    print(data.head())

    data['neg'] = data['review_content'].apply(lambda x:sia.polarity_scores(x)['neg'])
    data['neu'] = data['review_content'].apply(lambda x:sia.polarity_scores(x)['neu'])
    data['pos'] = data['review_content'].apply(lambda x:sia.polarity_scores(x)['pos'])
    data['compound'] = data['review_content'].apply(lambda x:sia.polarity_scores(x)['compound'])

    data['sentiment'] = np.where(data["compound"] >= -0.4, 1, 0)

    #data['verification'] = data['sentiment', 'review_rate'].apply(lambda x, y: verification(x, y))

    data['verification'] = data.apply(lambda x: verification(x.sentiment, x.review_rate), axis=1)

    good_predict = (data['verification'].sum())/(data['verification'].count())*100

    print('-----------------------------------------------------------------------------------------')
    print('\n')
    print(good_predict)
    print('\n')
    print('-----------------------------------------------------------------------------------------')

    #result = data.to_json(orient="split")

    return good_predict, data