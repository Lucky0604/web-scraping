#-*- coding: utf-8 -*-

from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

'''
for row in csvReader:
    print(row)

#['Name', 'Year']
#["Monty Python's Flying Circus", '1970']
#['Another Monty Python Record', '1971']
'''
dictReader = csv.DictReader(dataFile)
for row in dictReader:
    print(row)
#{'Year': '1970', 'Name': "Monty Python's Flying Circus"}
#{'Year': '1971', 'Name': 'Another Monty Python Record'}
#{'Year': '1972', 'Name': "Monty Python's Previous Record"}
