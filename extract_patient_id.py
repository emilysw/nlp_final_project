from collections import defaultdict
import numpy as np 
import math 
import re 
import pickle


### ======= This script extracts the patient_id from the icustayid found in the Sepsis.xls file 


# store the matching into a dictionary to look up in constant time! 

icustays_file = '/Users/emilywang/Desktop/new_cs282_final_project/ICUSTAYS.csv'

id_dict = defaultdict(list)

with open(icustays_file, 'r') as f:
	
	count = 0 
	for line in f: 
		if count == 0: 
			count += 1
			continue 
		row = line.split(",")
		subject_id = row[1]

		# add 200,000
		icustay_id = int(row[3])
		icustay_id -= 200000
		icustay_id = str(icustay_id)
		
		id_dict[icustay_id] = subject_id 

# There are 61532 unique icustayids 
print "Length of dictionary", len(id_dict)