{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import requests \n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "implementations = {'rca':'http://www.pbfcar.org/data.html' ,\n",
    "                   'kivu':'http://health.pbfsudkivu.org/data.html' ,\n",
    "                   'ethiopia':'http://www.pbfethiopia.org/data.html'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def get_page(url):\n",
    "    r = requests.get(url)\n",
    "    r = r.text\n",
    "    parsed_html = BeautifulSoup(r , 'html.parser')\n",
    "    page_body = parsed_html.select('body')\n",
    "    return page_body\n",
    "\n",
    "def get_indicators_names(indic_list):\n",
    "    indics = []\n",
    "    for i in range(len(indic_list)):\n",
    "        indics = indics + [indic_list[i].string]\n",
    "    return indics\n",
    "\n",
    "def get_fr_indicators(url):\n",
    "    page_body = get_page(url)\n",
    "    pca = page_body[0].findAll('a' , {'class':'indicator_pca'})\n",
    "    pca = get_indicators_names(pca)\n",
    "    pma = page_body[0].findAll('a' , {'class':'indicator_pma'})\n",
    "    pma = get_indicators_names(pma)\n",
    "    out = {'pca':pca , 'pma':pma}\n",
    "    return out\n",
    "\n",
    "def get_en_indicators(url):\n",
    "    page_body = get_page(url)\n",
    "    table_rows = page_body[0].findAll('li')\n",
    "    nrows = len(table_rows)\n",
    "    dframe = []\n",
    "    for row in range(1 , nrows) :\n",
    "        dframe = dframe + [table_rows[row].contents[len(table_rows[row]) - 1]]\n",
    "    return dframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "rca = get_fr_indicators(implementations['rca'])\n",
    "kivu = get_fr_indicators(implementations['kivu'])\n",
    "ethiopia = get_en_indicators(implementations['ethiopia'])\n",
    "ethiopia = ethiopia[6:15]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "list_indicators = {'rca':rca , 'kivu':kivu , 'ethiopia':ethiopia}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import json\n",
    "with open('data/indicators_lists.json', 'w') as f:\n",
    "    json.dump(list_indicators, f)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
