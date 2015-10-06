#python importer.py 
import import_sql
import csv 
import six 

errlog = 'C:\Users\djwilli\programs\data\importerrors.txt'
importFile = 'C:\Users\djwilli\programs\data\current.xls'

def usageMsg():
	print "you're doing it wrong."


#do I have a file args to open?
#If not open the test file importFile
for arg in sys.argv[1:]
	if isinstance(arg, six.string_types):
		loadFile(arg)
		latest = arg
		#In a real system we would move the original file aside as history
	else: 
		loadFile(importFile)
		latest = importFile

	#if I can't open the file prnt usage
	if not os.path.isfile(latest):
		print usageMsg()
		sys.exit()
	#
	#Partition Data 
	with open(latest, 'rb') as todayfile:
		readOneLine = csv.reader(todayfile, delimiter='|',quotechar'"')

		linedata = list()

		 headers = next(readOneLine)
		 linedata.append(line())
		 
		 for headers in cols:
		 	linedata.append(line())