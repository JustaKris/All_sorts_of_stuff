import csv
import os
import glob
import re

# FF lists
Desktop = ['AIO-DESKTOP', 'DESK', 'MICRO', 'TOWER', 'NETTOP']
Comp_Tablet = ['HYBRID CTAB', 'SLATE CTAB']
Netbook = ['MEDIABOOK']
Notebook = ['LAPTOP','DT REPLACEMENT','ULTRA MOBILE']

# Week - Month lookup 2020
month_lookup = {

	'1': 1,
	'2': 1,
	'3': 1,
	'4': 1,
	'5': 1,
	'6': 2,
	'7': 2,
	'8': 2,
	'9': 2,
	'10': 3,
	'11': 3,
	'12': 3,
	'13': 3,
	'14': 4,
	'15': 4,
	'16': 4,
	'17': 4,
	'18': 5,
	'19': 5,
	'20': 5,
	'21': 5,
	'22': 5,
	'23': 6,
	'24': 6,
	'25': 6,
	'26': 6,
	'27': 7,
	'28': 7,
	'29': 7,
	'30': 7,
	'31': 7,
	'32': 8,
	'33': 8,
	'34': 8,
	'35': 8,
	'36': 9,
	'37': 9,
	'38': 9,
	'39': 9,
	'40': 10,
	'41': 10,
	'42': 10,
	'43': 10,
	'44': 10,
	'45': 11,
	'46': 11,
	'47': 11,
	'48': 11,
	'49': 12,
	'50': 12,
	'51': 12,
	'52': 12
	
}

# Iterating trough each csv file in the directory
os.chdir("C:/Users/kristiyan.bonev/Desktop/Python Scripts/OnlineOffline/Raw Files")
extension = 'csv'

for file in glob.glob('*.{}'.format(extension)):
	current_file_name = file

	os.chdir("C:/Users/kristiyan.bonev/Desktop/Python Scripts/OnlineOffline/Raw Files")   # Change output directory
	
	# Open input file
	with open(current_file_name, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=';')
		
		# Create output file
		os.chdir("C:/Users/kristiyan.bonev/Desktop/Python Scripts/OnlineOffline")
		with open(current_file_name, 'w') as new_file:
			
			header = next(csv_reader)  # Saving file header
			additional = [{'Week' : 0}, {'Month' : 0}, {'Year' : 0}] # Updating with period columns
			for i in additional:
				header.update(i)
			
			# Creating output file
			csv_writer = csv.DictWriter(new_file, lineterminator='\n', fieldnames=header, delimiter=';')
			csv_writer.writeheader()
			
			# Modifying input data
			for row in csv_reader:
				if row['SEGMENTS'] in Desktop:
					row['SEGMENTS'] = 'Desktop'
				elif row['SEGMENTS'] in Comp_Tablet:
					row['SEGMENTS'] = 'Comp Tablet'
				elif row['SEGMENTS'] in Netbook:
					row['SEGMENTS'] = 'Netbook'
				elif row['SEGMENTS'] in Notebook:
					row['SEGMENTS'] = 'Notebook'
				else:
					row['SEGMENTS'] = 'Others'
				
				# Period setup
				week = re.findall(r' (\d{2}) ', row['Period'])
				year = re.findall(r' (\d{4})$', row['Period'])
				
				additional = [{'Week' : week[0]}, {'Month' : month_lookup[week[0]]}, {'Year' : year[0]}]
				
				for set in additional:
					row.update(set)
										
				csv_writer.writerow(row)
			