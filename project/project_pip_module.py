__version__ = "0.1.0"

import sys
import os
# user inputs and if else statements for validations and assessments
class Queries():
	
	join_type = raw_input("What type of JOIN would you like to use? " + "\n" + "1 = 1:1" + "\n" + "2 = 1:M" + "\n" + "3 = M:M" + "\n")
	join_type = int(join_type)
	
	table_count = raw_input("How many TABLES do you want to JOIN?? One, Two, or Three? ")
	table_count = int(table_count)
	
	column_count = raw_input("How many COLUMNS do you want to QUERY? One, Two, or Three? ")
	column_count = int(column_count)
	
	
	
	column_name = []
	table_name = []
	
	#FIRST BOUNDARY CHECK FOR THE COLUMN COUNT
	# if (column_count < 1 or column_count > 3):
	# 	column1_name = ''
	# 	column2_name = ''
	# 	column3_name = ''
	# 	print "Nope"
	
	def name_columns():
	
		if (column_count == 1):
			column1_name = number_columns1(column_name)
	
		elif (column_count == 2):
			column1_name = number_columns1(column_name)
			column2_name = number_columns2(column_name)
		
		else:
			column1_name = number_columns1(column_name)
			column2_name = number_columns2(column_name)
			column3_name = number_columns3(column_name)
	
	
	def name_tables():
	
		if (table_count == 1):
			table1_name = number_tables1(table_name) 
	
		elif (table_count == 2):
			table1_name = number_tables1(table_name)
			table2_name = number_tables2(table_name)
	
		else:
			table1_name = number_tables1(table_name)
			table2_name = number_tables2(table_name)
			table3_name = number_tables3(table_name)
	
	
	def number_columns1(self):
		column1_name = raw_input("What is your FIRST COLUMN name? ")
		column1_name = str(column1_name)
		column_name.append(column1_name)
		return column_name
	
	def number_columns2(self):
		column2_name = raw_input("What is your SECOND COLUMN name? ")
		column2_name = str(column2_name)
		column_name.append(column2_name)
		return column_name
	
	def number_columns3(self):
		column3_name = raw_input("What is your THIRD COLUMN name? ")
		column3_name = str(column3_name)
		column_name.append(column3_name)
		return column_name
	
	def number_tables1(self):
		table1_name = raw_input("What is your FIRST TABLE name? ")
		table1_name = str(table1_name)
		table_name.append(table1_name)
		return table_name
	
	def number_tables2(self):
		table2_name = raw_input("What is your SECOND TABLE name? ")
		table2_name = str(table2_name)
		table_name.append(table2_name)
		return table_name
	
	def number_tables3(self):
		table3_name = raw_input("What is your THIRD TABLE name? ")
		table3_name = str(table3_name)
		table_name.append(table3_name)
		return table_name
	
	#THIS IS FOR THE 1:1 
	if (join_type == 1):
		name_tables()
		name_columns()
		if (column_count == 1):
	#THIS IF FOR ONE COLUMN AND ONE TABLE
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], 
					table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
	#THIS IF FOR ONE COLUMN AND TWO TABLES
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0] )
	
	#THIS IF FOR ONE COLUMN AND THREE TABLES
			else:
				print """----------------------------------------------------------------------------------------\n
				SELECT %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0],
					table_name[2], table_name[2], table_name[1] )
	
		elif(column_count == 2):
	#THIS IF FOR TWO COLUMNS AND ONE TABLE
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
	
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], column_name[1], 
					table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
	#THIS IF FOR TWO COLUMNS AND TWO TABLES
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], column_name[1], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0] )
	#THIS IF FOR TWO COLUMNS AND THREE TABLES
			else:
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], column_name[1], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0],
					table_name[2], table_name[2], table_name[1] )
	
	#THIS IF FOR THREE COLUMNS AND ONE TABLE
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
		else:
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], column_name[1], column_name[2], 
					table_name[0],  
					table_name[0], table_name[0], table_name[0])
	
	#THIS IF FOR THREE COLUMNS AND TWO TABLES
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], column_name[1], column_name[2], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0])
	#THIS IF FOR THREE COLUMNS AND THREE TABLES
			else:
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				\n""" % (column_name[0], column_name[1], column_name[2], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0], 
					table_name[2], table_name[2], table_name[1])
	
	
	#THIS IS FOR THE 1:M
	if (join_type == 2):
		name_tables()
		name_columns()
		if (column_count == 1):
	#THIS IF FOR ONE COLUMN AND ONE TABLE
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
	#ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE ISSUE 
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
					SELECT %s 
					FROM %s
					JOIN %s ON %s.column_name_id = %s.column_name_id;
					
					connects where ids match
					-- example --
	
					JOIN sites ON clients.id = sites.client_id
					JOIN leads ON sites.id = leads.site_id;
					""" % (column_name[0], 
						table_name[0], 
						table_name[0], table_name[0], table_name[0] )
	
	#THIS IF FOR ONE COLUMN AND TWO TABLES
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
					SELECT %s 
					FROM %s
					JOIN %s ON %s.column_name_id = %s.column_name_id;
					
					connects where ids match
					-- example --
	
					JOIN sites ON clients.id = sites.client_id
					JOIN leads ON sites.id = leads.site_id;
					""" % (column_name[0], 
						table_name[0], 
						table_name[1], table_name[1], table_name[0] )
	#THIS IF FOR ONE COLUMN AND THREE TABLES
			else:
				print """----------------------------------------------------------------------------------------\n
					SELECT %s 
					FROM %s
					JOIN %s ON %s.column_name_id = %s.column_name_id
					JOIN %s ON %s.column_name_id = %s.column_name_id;
					
					connects where ids match
					-- example --
	
					JOIN sites ON clients.id = sites.client_id
					JOIN leads ON sites.id = leads.site_id;
					""" % (column_name[0], 
						table_name[0], 
						table_name[1], table_name[1], table_name[0], 
						table_name[2], table_name[2], table_name[1] )
	
	#THIS IF FOR TWO COLUMNS AND ONE TABLE
		elif(column_count == 2):
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
					SELECT %s, %s
					FROM %s
					JOIN %s ON %s.column_name_id = %s.column_name_id;
					
					connects where ids match
					-- example --
	
					JOIN sites ON clients.id = sites.client_id
					JOIN leads ON sites.id = leads.site_id;
					""" % (column_name[0], column_name[1], 
						table_name[0], 
						table_name[1], table_name[1], table_name[0] )
	#THIS IS FOR TWO COLUMNS AND TWO TABLES
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
					SELECT %s, %s
					FROM %s
					JOIN %s ON %s.column_name_id = %s.column_name_id;
					
					connects where ids match
					-- example --
	
					JOIN sites ON clients.id = sites.client_id
					JOIN leads ON sites.id = leads.site_id;
					""" % (column_name[0], column_name[1], 
						table_name[0], 
						table_name[1], table_name[1], table_name[0] )
	#THIS IS FOR TWO COLUMNS AND THREE TABLES
		else:
			print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s 
				FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				
				connects where ids match
				-- example --
	
				JOIN sites ON clients.id = sites.client_id
				JOIN leads ON sites.id = leads.site_id;
				""" % (column_name[0], column_name[1], column_name[2], 
					table_name[0], 
					table_name[1], table_name[1], table_name[0],
					table_name[2], table_name[2], table_name[1] )
	
	#THIS IS FOR THE M:M
	if (join_type == 3):
		name_tables()
		name_columns()
		if (column_count == 1):
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
			else:
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], column_name[2], table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
		elif(column_count == 2):
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], table_name[0], 
					table_name[1], table_name[1], table_name[0] )
	
			else:
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], table_name[0], 
					table_name[1], table_name[1], table_name[0],
					table_name[2], table_name[2], table_name[1] )
		else:
			if (table_count == 1):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], column_name[2], table_name[0], 
					table_name[0], table_name[0], table_name[0] )
	
			elif (table_count == 2):
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], column_name[2], table_name[0], 
					table_name[1], table_name[1], table_name[0] )
	
			else:
				print """----------------------------------------------------------------------------------------\n
				SELECT %s, %s, %s FROM %s
				JOIN %s ON %s.column_name_id = %s.column_name_id
				JOIN %s ON %s.column_name_id = %s.column_name_id;
				""" % (column_name[0], column_name[1], column_name[2], table_name[0], 
					table_name[1], table_name[1], table_name[0],
					table_name[2], table_name[2], table_name[1] )
	
	# if (__name__=="__main__"):
	# 	if (len(sys.argv) > 1):
	# 		if (sys.argv[1] == 'join_in'):
	# 			print sys.argv
	# 			query = Queries()
	# 			query.join_in()
	# 		else:
	# 			print 'You did not call a function'            
	
	   #this is like the router/controller}
