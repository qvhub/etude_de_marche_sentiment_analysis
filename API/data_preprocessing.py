import pandas as pd
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer

# Stop words list NLTK
stop_words = stopwords.words('french')


# Stop words list SPACY
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop

stop_words.append(fr_stop)

# Lemmatizer
#lemmatizer = WordNetLemmatizer()
lemmatizer = FrenchLefffLemmatizer()

# --- T O K E N I Z E R --- # 
tokenizer = RegexpTokenizer(r'\w+')

def google(x):
    if "(Avis d'origine)" in x:
        result = x.split("(Avis d'origine)")[0].replace("(Traduit par Google)","")
        return result
    else:
        return x

# --- C L E A N I N G - T E X T --- # 
def clean_text(text: str) -> str:
    """"
    Clean texte ponctuation, number, google traduction 
    """
    # Google trad EN 
    text = google(text)

    # Number
    text = re.sub('\d', '', str(text))
    
    # Punctuation
    text = re.sub('[^\w\s]', '', text)
    
    # Space
    text = re.sub('\s+', ' ', text)

    # Minuscule
    text = text.lower()

    return text

# --- L E M M A T I Z E --- # 
def lemmatize(tokens: list) -> list:

    for i in ["a", "v"]:
      tokens = list(map(lambda x: lemmatizer.lemmatize(x, i), tokens))

    return tokens


# --- P R E P R O C E S S I N G - F U N C T I O N  --- # 
def preprocess(txt: str) -> list:

    # Clean
    txt = clean_text(txt)

    # Tokens
    txt = tokenizer.tokenize(txt)

    # Stop_words
    txt = [i for i in txt if not i in stop_words]

    # Leammatizer 
    txt = lemmatize(txt)

    return txt

def data_preprocessed(data):

    data = data.dropna()

    data['reviews_processed'] = data['review_content'].apply(lambda x: preprocess(x))
 
    return data