import requests
import json
from random import randint
from tqdm.auto import tqdm
import time
import pandas as pd
import numpy as np


def review_scraping(city, business, nbr_result):
    #df = pd.read_csv('API/df_reims_restaurants_20.csv')
    
    # VARIABLES INIT 

    CITY = city
    BUSINESS = business
    PAGE = 7
    PER_PAGE = nbr_result

    # B U S I N E S S | I N F O S #
    # Init list #

    business_name = []
    business_address = []
    business_type = []
    business_count_review = []
    business_price = []
    business_global_rate = []
    city = []

    # R E V I E W | I N F O S #
    # Init list #

    user_name = []
    review_time = []
    review_content = []
    review_rate = []

    # url_search = f"https://www.google.fr/search?tbm=map&gl=fr&pb=!4m9!1m3!1d7764.500219424051!2d4.0902726528252495!3d49.21448590032151!2m0!3m2!1i1862!2i286!4f13.1!{PAGE}i{PER_PAGE}!10b1!12m8!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m65!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m50!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1sRPhQYOHWFcrRgwf19oKgBg%3A9!2zMWk6Myx0OjExODg3LGU6MixwOlJQaFFZT0hXRmNyUmd3ZjE5b0tnQmc6OQ!7e81!12e3!17sRPhQYOHWFcrRgwf19oKgBg%3A55!18e15!24m54!1m16!13m7!2b1!3b1!4b1!6i1!8b1!9b1!20b0!18m7!3b1!4b1!5b1!6b1!9b1!13b0!14b0!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!89b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i286!1m6!1m2!1i1812!2i0!2m2!1i1862!2i286!1m6!1m2!1i0!2i0!2m2!1i1862!2i20!1m6!1m2!1i0!2i266!2m2!1i1862!2i286!34m16!2b1!3b1!4b1!6b1!8m4!1b1!3b1!4b1!6b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m1!3b1!50m4!2e2!3m2!1b1!3b1!65m0!69i546&q="+CITY+"+"+BUISINESS
    # 

    url_search = f"https://www.google.fr/search?tbm=map&gl=fr&pb=!4m9!1m3!1d7764.500219424051!2d4.0902726528252495!3d49.21448590032151!2m0!3m2!1i1862!2i286!4f13.1!{PAGE}i{PER_PAGE}!10b1!12m8!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m65!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m50!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1sRPhQYOHWFcrRgwf19oKgBg%3A9!2zMWk6Myx0OjExODg3LGU6MixwOlJQaFFZT0hXRmNyUmd3ZjE5b0tnQmc6OQ!7e81!12e3!17sRPhQYOHWFcrRgwf19oKgBg%3A55!18e15!24m54!1m16!13m7!2b1!3b1!4b1!6i1!8b1!9b1!20b0!18m7!3b1!4b1!5b1!6b1!9b1!13b0!14b0!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!89b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i286!1m6!1m2!1i1812!2i0!2m2!1i1862!2i286!1m6!1m2!1i0!2i0!2m2!1i1862!2i20!1m6!1m2!1i0!2i266!2m2!1i1862!2i286!34m16!2b1!3b1!4b1!6b1!8m4!1b1!3b1!4b1!6b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m1!3b1!50m4!2e2!3m2!1b1!3b1!65m0!69i546&q="+CITY+"+"+BUSINESS


    def function_loop_list_review(var_1y, var_2y, data):
        proxy = {
        "http": '167.172.180.46:35301',
        "http": '103.78.252.105:8080',
        "http": '91.149.203.9:3128'
        }

        headers = {
        'authority': 'www.google.com',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36',
        'accept': '*/*',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.google.com/',
        'accept-language': 'en-US,en;q=0.9',
        }

        payload = {}
        ten = 0
        while True:
            print(ten)
            url_review_list_per10 = f"https://www.google.fr/maps/preview/review/listentitiesreviews?authuser=0&hl=fr&gl=fr&pb=!1m2!1y{var_1y}!2y{var_2y}!2m2!1i{ten}!2i99!"

            response_url_review_list = requests.request("GET", url_review_list_per10, headers=headers, data=payload, proxies=proxy)
            
            print(url_review_list_per10)
            
            r_review = response_url_review_list.text[4:]
            r_review = r_review.replace("null,",'"",')
            #r_review = json.dumps(r_review)
            data_review = json.loads(r_review)
            # liste des review dans la selection des 10 
            ll = len(data_review[2])
            
            if ll == 0:
                break
                
            print(ll)

            for i in tqdm(range(0,ll)):

                ### *** --- B U S I N E S S | I N F O S --- *** ####

                # business name
                try:
                    b_name = data[0][1][0][14][11]
                except:
                    b_name = data[0][0]
                print(b_name)
                business_name.append(b_name)

                # business address
                try:
                    address = data[0][1][0][14][39]
                except:
                    address = np.NaN    
                business_address.append(address)

                # business type
                try:
                    b_type = data[0][1][0][14][39]
                except:
                    b_type = np.NaN   
                business_address.append(b_type)

                # business price
                try:
                    price = data[0][1][0][14][4][4]
                except:
                    price = np.NaN    
                business_price.append(price)

                # business rate
                try:
                    global_rate = data[0][1][0][14][4][7]
                except:
                    global_rate = np.NaN    
                business_global_rate.append(global_rate)

                # business count review
                try:
                    c_r = data[0][1][0][14][4][8]
                except:
                    c_r = np.NaN    
                business_count_review.append(c_r)

                ### *** --- R E V I E W | I N F O S --- *** ####

                #Name
                try:
                    u_name = data_review[2][i][0][1]
                except:
                    u_name = np.NaN

                print(u_name)
                user_name.append(u_name)

                #Date
                try:
                    date_time = data_review[2][i][1]
                except:
                    date_time = np.NaN

                review_time.append(date_time)

                #Content
                try:
                    review = data_review[2][i][3]
                except:
                    review = np.NaN

                review_content.append(review)

                #Rate
                try:
                    rate = data_review[2][i][4]
                except:
                    rate = np.NaN

                review_rate.append(rate)

                #Take a break

            # add 10 at ten for charge the another link with review list  
            ten += 99
            # take a break 
            time.sleep(randint(3,13))

    def get_url(url):
        proxy = {
        "http": '167.172.180.46:35301',
        "http": '103.78.252.105:8080',
        "http": '91.149.203.9:3128'
        }
        payload={}
        headers = {
        'authority': 'www.google.com',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36',
        'accept': '*/*',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.google.com/',
        'accept-language': 'en-US,en;q=0.9',
        }

        response = requests.request("GET", url, headers=headers, data=payload, proxies=proxy)

        #response = requests.request("GET", url, headers=headers, data=payload)

        response = response.text[4:]
        response = response.replace("null", '""')

        parsed = json.loads(response)

        return parsed

    # Get all commerce from google map search

    # Call function get_url for get the url search withe your own parameters 
    parsed = get_url(url_search)

    # Get commerce list from json into index 0 and 1
    commerce_list = parsed[0][1]

    # Init commerce adress list and url foreach search of commerce 
    commerce_adress_list = []
    commerce_url_search_list = []

    NUMPOST = 99
    PAGE = 99

    commerce_url_solo = f"https://www.google.fr/search?tbm=map&gl=fr&pb=!4m9!1m3!1d7764.500219424051!2d4.0902726528252495!3d49.21448590032151!2m0!3m2!1i1862!2i286!4f13.1!{PAGE}i{PER_PAGE}!10b1!12m8!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!19m4!2m3!1i360!2i120!{NUMPOST}i{NUMPOST}!20m65!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m50!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1sRPhQYOHWFcrRgwf19oKgBg%3A9!2zMWk6Myx0OjExODg3LGU6MixwOlJQaFFZT0hXRmNyUmd3ZjE5b0tnQmc6OQ!7e81!12e3!17sRPhQYOHWFcrRgwf19oKgBg%3A55!18e15!24m54!1m16!13m7!2b1!3b1!4b1!6i1!8b1!9b1!20b0!18m7!3b1!4b1!5b1!6b1!9b1!13b0!14b0!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!89b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i286!1m6!1m2!1i1812!2i0!2m2!1i1862!2i286!1m6!1m2!{NUMPOST}i{NUMPOST}!{NUMPOST}i{NUMPOST}!2m2!1i1862!{NUMPOST}i{NUMPOST}!1m6!1m2!{NUMPOST}i{NUMPOST}!2i266!2m2!1i1862!2i286!34m16!2b1!3b1!4b1!6b1!8m4!1b1!3b1!4b1!6b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m1!3b1!50m4!2e2!3m2!1b1!3b1!65m0!69i546&q="

    cll = len(commerce_list)

    for i in range(1,cll):
        commerce_temp = parsed[0][1][i][14][18]
        commerce_temp = commerce_temp.replace(',', '')
        commerce_temp = commerce_temp.replace(' ', '+')
        commerce_adress_list.append(commerce_temp)
        commerce_url_search_list.append(commerce_url_solo+commerce_temp)
        # time.sleep(randint(0,5))



    for i in tqdm(commerce_url_search_list):
        
        #print(i)
        try:
            data = get_url(i)
        except:

            df = pd.DataFrame({
            'business_name' : business_name,
            #'business_address' : business_address,
            #'business_type' : business_type,
            'business_count_review' : business_count_review,
            'business_price' : business_price,
            'business_global_rate' : business_global_rate,
            #'city' = city
            'user_name' : user_name,
            'review_time' : review_time,
            'review_content' : review_content,
            'review_rate' : review_rate
            })

            df.to_csv(f'df_{CITY}_{BUSINESS}_{PER_PAGE}_BACKUP.csv')
            print('sauvegarde, problemes')

        # Entre into each business 
        try:
            var_1y = data[0][1][0][14][37][0][0][29][0]
            print(var_1y)

            var_2y = data[0][1][0][14][37][0][0][29][1]
            print(var_2y)

            function_loop_list_review(var_1y, var_2y, data)
            print('ok function loop')
        except:
            pass   

        time.sleep(randint(2,10))

    import pandas as pd

    df = pd.DataFrame({
    'business_name' : business_name,
    #'business_address' : business_address,
    #'business_type' : business_type,
    'business_count_review' : business_count_review,
    'business_price' : business_price,
    'business_global_rate' : business_global_rate,
    #'city' = city
    'user_name' : user_name,
    'review_time' : review_time,
    'review_content' : review_content,
    'review_rate' : review_rate
    })

    df.to_csv(f'df_{CITY}_{BUSINESS}_{PER_PAGE}.csv')
    

    return df