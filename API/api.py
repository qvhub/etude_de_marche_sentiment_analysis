# import main Flask class and request object
from flask import Flask, request
import nlp_nltk
import pandas as pd

import review_scraping as rs 
import data_preprocessing
import lda_gensim
import lda_preprocessing as lp

import json

# create the Flask app
app = Flask(__name__)
    
@app.route('/etude-de-marche')
def etude_de_marche():
    # if key doesn't exist, returns None
    city = request.args.get('city')
    business = request.args.get('business')
    number_result = request.args.get('nbr-result')
    b_name = request.args.get('b-name')
    args_nlp = request.args.get('nlp')
    args_lda = request.args.get('lda')
    #num_topics = request.args.get('nbt')

    scraping_data = rs.review_scraping(city, business, number_result)

    print(scraping_data.info())

    name_commerce = scraping_data['business_name'].unique()
    print('-------------------------------------------------------------------------------------------')
    print('\n')
    print(name_commerce)
    print('\n')
    print('-------------------------------------------------------------------------------------------')
  

    if b_name:
        scraping_data = scraping_data.loc[scraping_data['business_name'] == b_name]
        #name_commerce = ""

    processing = data_preprocessing.data_preprocessed(scraping_data)

     # N L P

    if args_nlp == "nltk":
        good_predict, result_nlp_nltk = nlp_nltk.sentiment_analysis(processing)
        global_satisfaction =  ((result_nlp_nltk['sentiment'].sum())/(result_nlp_nltk['sentiment'].count()))*100

    if args_nlp == "camenbert":    
        print('W I P')

    # L D A 

    if args_lda == "gensim":
        name_commerce = processing['business_name'].unique()
        print('-------------------------------------------------------------------------------------------')
        print('\n')
        print(name_commerce)
        print('\n')
        print('-------------------------------------------------------------------------------------------')

        ldap = lp.lda_preprocessing(processing)
        lda_gen_pos, lda_gen_neg = lda_gensim.lda_gensim_topics(ldap, 2)

    if args_lda == "sklearn":
        print('W I P')

    data_select = result_nlp_nltk[['business_name', 'sentiment']]
    data_select = data_select.groupby(by=["business_name"]).mean()

    render = {
            "Taux de satisfaction": global_satisfaction,
            "city": city,
            "business tpye": business,
            "business liste": data_select.to_json(),
            "Positif": lda_gen_pos,
            "Negatif": lda_gen_neg,
            }

    #return 'Business{} LDA{}'.format(name_commerce, lda_gen)
    return render

@app.route('/')
def bienvenu():
    var_txt = "Bienvenu sur * * * V L A - - l'A P I * * * et * * * V L A les resultats * * *"
    return var_txt

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

