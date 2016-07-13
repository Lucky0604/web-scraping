# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import datetime
import random

'''
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')
'''

'''
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

'''
# revise the code slightly to retrieve only the desired article links
for link in bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

'''
1, A single function, getLinks , that takes in a Wikipedia article URL of the form /
wiki/<Article_Name> and returns a list of all linked article URLs in the same
form
2, A main function that calls getLinks with some starting article, chooses a random
article link from the returned list, and calls getLinks again, until we stop the
program or until there are no article links found on the new page.
'''
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
