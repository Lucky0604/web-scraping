#-*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://cnodejs.org/')
bsObj = BeautifulSoup(html, 'html.parser')

content = bsObj.find('div', {'id': 'topic_list'}).findAll('a', {'class': 'topic_title'})

for title in content:
	print(title.get_text())