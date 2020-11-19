 ###################################################################
# Test script to validate Output CSV generated after normalizer.py
# Usage: python testScript.py -o <output_csv_filename.csv>
# NOTE: 1. Python 3.7.2 required.
#		2. input_file needs to updated depending on the filename.
# Script can be used on Windows and Linux
# Author: Shivansh Mehta, shivansh.mehta@gmail.com
####################################################################


import argparse
from datetime import datetime
from dateutil import tz
import csv
import sys
import os

input_file = 'output.csv'


def verifyTimeStampFormat(timestamp):
	
	try: 
		datetimeObj1 = datetime.strptime(timeStamp, '%Y-%m-%dT%H:%M:%S%z')
	# end try
	except (ValueError):
		print('ERROR! Invalid timestamp format: {}'.format(timeStamp))
		sys.exit(-1)
	# end except

	if timeStamp.count('-') == 4 or timeStamp.count('+') == 1:
		try:
			datetimeObj2 = datetime.strptime(timeStamp, '%Y-%m-%dT%H:%M:%S')
		# end try
		except (ValueError):
			print("ERROR! Invalid timestamp format: {}".format(timeStamp))
			sys.exit(-1)
		# end except
	# end if timeStamp.count('-') == 4 or timeStamp.count('+') == 1	
	
###########################################
# Verify timestamp field format of the CSV
# 
# Args: timestamp: time stamp field in CSV
#
# Returns: Nothing
###########################################
def verifyTimeZone(timestamp):
	
	datetimeObj = datetime.strptime(timeStamp, '%Y-%m-%dT%H:%M:%S%z')
	if ((datetimeObj.tzname() != 'UTC-04:00') and (datetimeObj.tzname() != 'UTC-05:00')):
		raise ValueError("ERROR! Invalid time-zone value: {}".format(datetimeObj.tzname()))  
	# end if ((datetimeObj.tzname() != 'UTC-04:00') and (datetimeObj.tzname() != 'UTC-05:00'))
###########################################
# Verify zipcode format of the CSV
# 
# Args: zipcode: zipcode field in CSV
#
# Returns: Nothing
###########################################
def verifyZipCodeFormat(zipCode):

	if len(zipCode) < 5:
		raise Exception("ERROR! Invalid Zipcode Format.")
	# end if len(zipCode) < 5:

###########################################
# Verify Full Name field of the CSV
# 
# Args: fullName: Full name field in CSV
#
# Returns: Nothing
###########################################
def verifyFullNameCase(fullName):

	if not fullName.isupper():
		raise Exception("ERROR! Invalid Full Name Format.")
	# end if not fullName.isupper()

###########################################
# Verify Address field of the CSV
# 
# Args: address: address field in CSV
#
# Returns: Nothing
###########################################
def verifyAddress(address):

	if not isinstance(address, str):
		raise Exception("ERROR! Invalid Address type.")
	# if not isinstance(address, str)

###########################################
# Verify Total Duration field of the CSV
# 
# Args: totalDuration: total duration field in CSV
#		fooDuration: fooDuration field in CSV
#		barDuration: barDuration field in CSV
#
# Returns: Nothing
###########################################
def verifyTotalDuration(totalDuration, fooDuration, barDuration):
	fooDuration = float(fooDuration)
	barDuration = float(barDuration)
	totalDuration = float(totalDuration)
	total = fooDuration + barDuration
	if (totalDuration != total):
		print("ERROR! Incorrect Total Duration value {}".format(totalDuration))
		sys.exit(-1)
	# if (totalDuration != total)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output_file', required=True, help="Output CSV file")
	args, argv = parser.parse_known_args()
	output_file = args.output_file
	
	msg = "\nVerifying given requirements..."
	print(msg)

	msg = "\nChecking of given file path exists..."
	print(msg)

	if not os.path.exists(input_file):
		raise IOError("\nERROR! CSV File not Found.")
	# end if not os.path.exists(input_file)

	msg = "\nChecking if CSV file is not empty..."
	print(msg)
	if os.stat(input_file).st_size > 0:

		with open(input_file, newline='', encoding='utf-8') as csvfile:
			rows = list(csv.DictReader(csvfile))
			for row in rows:
				timeStamp  = row['Timestamp']
				zipCode = row['ZIP'] 
				fullName = row['FullName']
				address = row['Address']
				fooDuration = row['FooDuration']
				barDuration = row['BarDuration']
				totalDuration = row['TotalDuration']
				verifyTimeStampFormat(timeStamp)
				verifyTimeZone(timeStamp)
				verifyZipCodeFormat(zipCode)
				verifyFullNameCase(fullName)
				verifyAddress(address)
				verifyTotalDuration(totalDuration, fooDuration, barDuration)
			# end for row in rows
	# end if os.stat(input_file).st_size > 0
	else:
		msg = "\nERROR! CSV File is Empty."
		print(msg)
		sys.exit(-1)
	# end else
	msg = "Requirements validated."
	print(msg)
	sys.exit(0)
# end if __name__ == "__main__"





				





