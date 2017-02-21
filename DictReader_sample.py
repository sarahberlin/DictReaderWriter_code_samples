###reading a csv with DictReader
#DictReader loops through every row in the csv, creates a dictionary for that row, and then appends that dictionary to a list
#each dictionary in the list will have the same keys

import csv
from csv import DictWriter, DictReader

#empty list that each dictionary will be added to
dictList =[]

#basic file handling with the addition of DictReader
with open('seattle_council.csv',"r") as seattle_file:
	reader = csv.DictReader(seattle_file)
	for row in reader:
		dictList.append(row)
