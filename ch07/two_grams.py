#-*- coding: utf-8 -*-

# In linguistics, an n-gram is a sequence of n words used in text or speech

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
'''
Using some regular expressions to remove escape characters (such as \n ) and filtering
to remove any Unicode characters
'''
def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i: i + n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print('2-grams count is: ' + str(len(ngrams)))