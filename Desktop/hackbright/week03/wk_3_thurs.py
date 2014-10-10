import csv
print "i'm adding something at the top!"

# # with open('sweep.csv') as f:
# # 	reader = csv.DictReader(f)
# # 	for row in reader:
# # 		if reader.line_num < 10:
# # 			print row

# with open('mini.csv') as f:
# 	reader = csv.reader(f)



############### SCL SECTION COUNTER ######################################
# with open ('sweep.csv') as f:
# 	reader = csv.DictReader(f)
# 	for row in reader:
# 		if reader.line_num <4:
# 			print row
# days_counts = {
# 	'Mon': 0,
# 	'Tues': 0,
# 	'Wed': 0,
# 	'Thu': 0,
# 	'Fri': 0,
# 	'Sat': 0,
# 	'Sun': 0 ,
# 	'Holiday': 0 
# 	}


# with open ('sweep.csv') as f:
# 	reader = csv.DictReader(f)
# 	for row in reader:
# 		day = row['WEEKDAY']
# 		for i in day:
# 			days_counts[day] +=1

# for d in days_counts:
# 	print"{} blocks swept on {}".format(days_counts[d], d)

######################################## WHEN IS STREET BEING SWEPT##########################
# fav_street ="Baltimore Way"
# house_number = 3122


# # def find_block(address, row):
# # 	weekday = row[1]
# # 	street = row[5]
# # 	side = row[4]
# # 	left_from = int(row[14])
# # 	left_to = int(row[15])	
# # 	right_to = int(row[16])
# # 	right_from = int(row[17])

# # 	if left_from< address< left_to:
# # 		print street

# # 		print left_from, left_to, side, weekday
# # 		print right_from, right_to, side, weekday	
# # 		return True
# # 	else:
# # 		return False

# # street_found = False

# # with open ('sweep.csv') as f:
# # 	reader = csv.reader(f)
# # 	for row in reader:
# # 		street = row[5]
# # 		if street == fav_street:
# # 		 	found = find_block(house_number, row)
# # 		 	if found == True:
# # 		 		street_found = True
		 	
# # if street_found == False:
# # 	print "This street was never found"
# # print "i found", street_found


# with open('sweep.csv') as f:
# 	reader = csv.DictReader(f)
# 	for row in reader:
# 		street_name = row['STREETNAME']
# 		if fav_street in ['STREETNAME']:
# 			print "hi"

# # def swept_tomorrow(street_name, house_number):
# # 	if 
























