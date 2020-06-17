from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import datetime
import nltk
import re
import pymongo

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

CSV_PATH = '/data/countries.csv'

all_headlines = []

# Load CSV of countries and headlines

# Put this into Mongo:
url_list = ['https://www.arubatoday.com/',
            'https://tolonews.com/',
            'https://www.angop.ao/angola/en_us/index.html',
            'http://theanguillian.com/',
            'https://albaniandailynews.com/',
            'https://all-andorra.com/',
            'https://www.khaleejtimes.com/',
            'https://www.batimes.com.ar/',
            'https://armenpress.am/eng/',
            'https://samoanews.com/',
            'https://antiguaobserver.com/',
            'http://www.viennatimes.com/',
            'https://www.azernews.az/',
            ]
headline_tags = ['h1', 'h2', 'h3']
min_words = 3


def filter_headline(headline):
    # Need to copy object?
    text = headline['text']
    # print(text)
    words = text.split()
    if len(words) < min_words:
        return None

    # Look for verb
    tokenized = [a for a in nltk.word_tokenize(text) if a.isalpha()]
    pos_tags = set([x[1] for x in nltk.pos_tag(tokenized)])
    verb_tags = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
    # If there is a verb:
    if verb_tags.intersection(pos_tags):
        return headline
    return None

    #verb_tag_re = re.compile('(^V*)')
    # Checks if a verb has been tagged:
    #print(list(filter(verb_tag_re.search, pos_tags)))
    # if not filter(verb_tag_re.match, pos_tags):  # ' '.join(pos_tags)):
    #print('no verb', '\n\n\n')
    #    return None


for url in url_list:
    page = requests.get(url).text
    soup = BeautifulSoup(page)

    headlines = [
        {'tag_name': el.name,
         'text': el.text.strip()} for el in soup.find_all(headline_tags)
    ]

 #   for headline in headlines:
 #       obj = {
 #           'element_name': headline.name,
 #           'text': headline.txt,
 #           'timestamp': datetime.now(),
 #           'source': url
 #       }

    # insert into mongo/sqlite

    # Find the first dict in a list of dicts where one of the dict values is a certain value
    headlines_filtered = [filter_headline(
        headline) for headline in headlines]  # remove Nones
    headlines_filtered = [h for h in headlines_filtered if h]

    for tag in headline_tags:
        tag_list = list(
            filter(lambda x: x['tag_name'] == tag, headlines_filtered))
        if tag_list:
            chosen_headline = tag_list[0]
            all_headlines.append(chosen_headline)
            break

    # Or just select the chosen headline in SQL?


def get_data():
    pass
