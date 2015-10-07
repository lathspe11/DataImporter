#python importer.py 
import import_sql
import csv 
import sys
import os

errlog = 'C:\\Users\\djwilli\\programs\\data\\importerrors.txt'
importFile = 'C:\\Users\\djwilli\\documents\\programs\\data\\initdata.txt'

def usageMsg():
	print("you're doing it wrong.")

def validFile(apath):
	#if I can't open the file prnt usage
	if not os.path.isfile(apath):
		usageMsg()
		print(apath + ' Not a valid path. Exiting')
		sys.exit()
	#

headers = list()
linedata = list()
partdict = {}
vuedict = {}

def readImport(openme):
	with open(openme, 'r') as todayfile:
		readOneLine = csv.reader(todayfile, delimiter='|',quotechar='"')

		#Strip off the header
		headers = next(readOneLine)
		print(headers[0:])
		#Build lists for the keys
		for col in headers:
			linedata.append(list())
			print(col)
		rowcnt = 0

		for aline in readOneLine:
			key = aline[0] + '|' + aline[1] + '|' + aline[3]
			yr,mnth,day = aline[3].split('-')
			partnam = yr+"\\"+mnth
			if partnam in partdict.keys():
				partdict[partnam] += 1
			else:
				partdict[partnam] = 1
			print(key + " %s" % ' '.join(str(x) for x in aline))
			vuedict[key] = aline

		print("number of partitions" + str(len(partdict)))
		
			
#do I have a file args to open?
#If not open the test file importFile
print("This value will = 2 if in a command shell with an arg is given")
cntargs = len(sys.argv)
print(cntargs)

if cntargs < 2 :
	validFile(importFile)
	latest = importFile
	readImport(latest)
else :
	for arg in sys.argv[1:]:
		if isinstance(arg, str) or isinstance(arg, unicode):
			validFile(arg)
			latest = arg
			#In a real system we would move the original file aside as history
			
		#
		#Partition Data 

print('Program Completed')