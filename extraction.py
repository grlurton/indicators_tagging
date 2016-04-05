import requests
from bs4 import BeautifulSoup
import pandas as pd

implementations = {'rca':'http://www.pbfcar.org/data.html' ,
                    'kivu':'http://health.pbfsudkivu.org/data.html' ,
                    'ethiopia':'http://www.pbfethiopia.org/data.html'}


def get_page(url):
    r = requests.get(url)
    r = r.text
    parsed_html = BeautifulSoup(r , 'html.parser')
    page_body = parsed_html.select('body')
    return page_body

def get_indicators_names(indic_list):
    indics = []
    for i in range(len(indic_list)):
        indics = indics + [indic_list[i].string]
    return indics

def get_fr_indicators(url):
    page_body = get_page(url)
    pca = page_body[0].findAll('a' , {'class':'indicator_pca'})
    pca = get_indicators_names(pca)
    pma = page_body[0].findAll('a' , {'class':'indicator_pma'})
    pma = get_indicators_names(pma)
    out = {'pca':pca , 'pma':pma}
    return out

def get_en_indicators(url):
    page_body = get_page(url)
    table_rows = page_body[0].findAll('li')
    nrows = len(table_rows)
    dframe = []
    for row in range(1 , nrows) :
        dframe = dframe + [table_rows[row].contents[len(table_rows[row]) - 1]]
    return dframe

rca = get_fr_indicators(implementations['rca'])
kivu = get_fr_indicators(implementations['kivu'])
ethiopia = get_en_indicators(implementations['ethiopia'])
ethiopia = ethiopia[6:15]

list_indicators = {'rca':rca , 'kivu':kivu , 'ethiopia':ethiopia}

import json
with open('data/indicators_lists.json', 'w') as f:
    json.dump(list_indicators, f)
