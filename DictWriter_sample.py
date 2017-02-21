###writing to a csv with DictWriter

#takes a list of dictionaries and turns it into a csv
#each dictionary in the list should have the same keys, the keys then become the top row in the csv

#dictList is the list of dictionaries
dictList = [{'website': 'https://www.seattle.gov/council/meet-the-council#herbold', 'electoral.district': 'Seattle City Council District 1', 'UID': 'CIe00919', 'OCDID': 'ocd-division/country:us/state:wa/place:seattle/council_district:1', 'twitter': '', 'office.name': 'Council, District 1', 'phone': '', 'state': 'WA', 'facebook': '', 'body represents - muni': 'Seattle', 'address': '', 'Body Name': '', 'email': '', 'official.name': 'Lisa Herbold'}, {'website': 'https://www.seattle.gov/council/meet-the-council#harrell', 'electoral.district': 'Seattle City Council District 2', 'UID': 'CIe00920', 'OCDID': 'ocd-division/country:us/state:wa/place:seattle/council_district:2', 'twitter': '', 'office.name': 'Council, District 2', 'phone': '', 'state': 'WA', 'facebook': '', 'body represents - muni': 'Seattle', 'address': '', 'Body Name': '', 'email': '', 'official.name': 'Bruce Harrell'}, {'website': 'https://www.seattle.gov/council/meet-the-council#sawant', 'electoral.district': 'Seattle City Council District 3', 'UID': 'CIe00921', 'OCDID': 'ocd-division/country:us/state:wa/place:seattle/council_district:3', 'twitter': '', 'office.name': 'Council, District 3', 'phone': '', 'state': 'WA', 'facebook': '', 'body represents - muni': 'Seattle', 'address': '', 'Body Name': '', 'email': '', 'official.name': 'Kshama Sawant'}, {'website': 'https://www.seattle.gov/council/meet-the-council#johnson', 'electoral.district': 'Seattle City Council District 4', 'UID': 'CIe00922', 'OCDID': 'ocd-division/country:us/state:wa/place:seattle/council_district:4', 'twitter': '', 'office.name': 'Council, District 4', 'phone': '', 'state': 'WA', 'facebook': '', 'body represents - muni': 'Seattle', 'address': '', 'Body Name': '', 'email': '', 'official.name': 'Rob Johnson'}]

#fieldnames is the list of keys that will become the top row in the csv
fieldnames = ['UID','state','body represents - muni','Body Name','electoral.district','office.name','official.name', 'address','phone','website', 'email', 'facebook', 'twitter', "OCDID"]

#basic file handling with the addition of DictWriter
with open('seattle_council.csv','w') as seattle_council_file: 
	csvwriter = csv.DictWriter(seattle_council_file, delimiter=',', fieldnames=fieldnames)
	csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
	for row in dictList:
	    csvwriter.writerow(row)
