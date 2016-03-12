import sys
import os

class Tax():
	def tax_evasion(self):
		print "evaded taxes"
		last_time = raw_input('how much money did you make?')
		print last_time
		file_name = raw_input('name of your tax file?')
		os.system('echo ' + file_name)

if __name__=='__main__':
	if len(sys.argv) > 1: 
		if sys.argv[1]=='tax_evasion':
			tax = Tax()
			tax.tax_evasion()
	else:
		print "you didn't call a function"