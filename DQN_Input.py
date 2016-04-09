'''
Module to read stock price data from csv files
'''
# General
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# System import
import csv

# Read the CSV file and return the DictReader pointer of it
def ReadCSV(csv_filename):
	DataSourceFile = open(csv_filename)
	reader = csv.DictReader(DataSourceFile)
	return reader
	'''
	try:
		for row in reader:
			print(row['Open'], row['Close'])
	except csv.Error as e:
		sys.exit('file %s, line %d: %s' % (DS_filename, reader.line_num, e))
	'''

