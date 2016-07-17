#-*- coding: utf-8 -*-

# retrieve an HTML table and write it as a CSV file.
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, 'html.parser')
# the main comparison table is currently the first table on the page
table = bsObj.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('./files/editors.csv', 'wt')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()