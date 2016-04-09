'''
Main module
'''
# General
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# default modules
from datetime import datetime
# 3rd party library
import numpy as np
import tensorflow as tf
# Project modules
import DQN_Input as dqn_input
import DQN_Network as dqn_net

# Constants 
DATA_PATH = 'Data/'
DATA_FILE = 'YahooDaily.csv'

def Run():
	print("Program starts %s." % (datetime.now()))
	#array = np.random.rand(3,3)
	#print(array)
	counter = 0
	price_open = np.zeros[10000]
	#price_close = []
	reader = dqn_input.ReadCSV(DATA_PATH+DATA_FILE)
	for row in reader:
		price_open[counter] = row["Open"]
		counter += 1
		print("Step: %s" % (counter))
	#print(array)
	print("Program ends %s." % (datetime.now()))
	
if __name__ == "__main__":
	Run()
