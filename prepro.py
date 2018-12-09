from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import nltk
nltk.download('punkt')
import string
from nltk.stem.snowball import SnowballStemmer


def stop(s):
    s = words = word_tokenize(s)
    it_stops = set(stopwords.words('italian'))
    
    wordsFiltered = []

    for w in s:
        if w not in it_stops:
            wordsFiltered.append(w)
    return wordsFiltered


def punctuation(l):
    exclude = set(string.punctuation)
    for el in l:
        if el in exclude:
            l.remove(el)
    return l


def stemmer(l):
    stemmer = SnowballStemmer("italian")
    result = []
    for el in l:
        
        r = stemmer.stem(el)
        result.append(r)
        
    return result