Market research by sentiment analysis

By Alexis Perpète, Nicolas Chevalier, Quentin Vautier

--- Folder tree ---

API folder

## GENERAL INFORMATIONS :

We work for a company offering a service to obtain market research to its users.
The goal is to create an API that will provide an overview of the feelings of our users' prospects (via Trustpilot, Google,...), towards competing companies.
Once the API is ready, it will be connected to a new dashboard developed in parallel with the web division.
The API will at least allow to retrieve, for a given domain and location, a json proposing the necessary data to establish an efficient dashboard.
To do this, our API will return the complete reviews of the establishments, will present the most significant words, will return each feeling by differentiating them, suggestion of the ranking of the establishments according to the customers' reviews

# SETUP :

Download our requirement and install all modules in virtual environnement (recommended)

````pip install -r requirement.txt```


# API :

When you use the api, don't forget to click on « Running on http://127.0.0.1:5000/ »
add paramters for city, business type, number of results per requests (max 999), kind of NLP and LDA.

In this way you can get sentiments annalysis for :http://127.0.0.1:5000/etude-de-marche?city=reims&business=restaurant&nbr-result=2&nlp=nltk&lda=gensim
