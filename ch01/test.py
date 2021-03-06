# coding: utf-8

'''
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
'''

# use beautifulsoup4
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj)
'''

# handle exception
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None

	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
	print('Title could not be found.')
else:
	print(title)
