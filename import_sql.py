#file and directory operations for importer
datapath = 'C:\\Users\\djwilli\\documents\\programs\\data\\'
vuedata = 'vuedata.txt'
#New Partition
import os
import errno
import csv
import sys

def verifyDataFolder():
	try :
		os.makedirs(datapath)
		return True

	except OSError as exception:
		if not os.path.isdir(datapath):
			raise
		return False

def verifyDataPath(mypath):
	newpath = datapath + mypath
	print("verifyDataPath(%s)" % newpath)

	try :
		os.makedirs(newpath)
		return True

	except OSError as exception:
		if not os.path.isdir(newpath):
			raise
	return False

#Is file there?
def validFile(apath):
	#if I can't open the file prnt usage
	if not os.path.isfile(apath):
		print(apath + ' Not a valid path. Exiting')
		sys.exit()
	#

#Does Partition exist? make sure
def ifPartition(date):
	print("ifPartition(%s)" % date)
	#Is date arg valid?
	yr,mnth,day = date.split('-')
	#Validate date has a partition
	newpath = yr + "\\" + mnth
	if verifyDataPath(yr):
		print ("made dir " + yr)
	else:
		print (yr + " already exists")
	if verifyDataPath(newpath):
		print ("made dir " + newpath)
	else:
		print (newpath + "already exists")
	return datapath + newpath

#Get partition name
def getPartitionName(date):
	#Is date arg valid?
	yr,mnth,day = date.split('-')
	#Validate date has a partition
	newpath = yr + "\\" + mnth
	return newpath

def writePartition(importDict,dtpath):
	newpath = datapath + dtpath + "\\" + vuedata
	print(">%s<" % newpath)
	try:
		partitionFile = open(newpath,"w")

		for dlist in importDict.values():
			#yr,mnth,day = dlist[3].split('-')
			cmpdt =  getPartitionName(dlist[3])
			if dtpath == cmpdt:
				outline = '|'.join(dlist) + "\n"
				print("write %s" % outline)
				partitionFile.write(outline)
		partitionFile.close()
	except IOError:
		print("writePartition Failed to open %s" % newpath)

def openPartition(dtpath):
	newpath = datapath + dtpath + "\\" + vuedata
	dsDict = {}
	try:
		with open(newpath, 'r') as todayfile:
			readDSLine = csv.reader(todayfile, delimiter='|',quotechar='"')
			
			for aline in readDSLine:
				key = aline[0] + '|' + aline[1] + '|' + aline[3]
				dsDict[key] = aline

			todayfile.close()
			return dsDict

	except IOError:
		print("OpenPartition Failed to open %s" % newpath)