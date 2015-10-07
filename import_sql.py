#SQL for importer
datapath = 'C:\\Users\\djwilli\\Documents\\Programs\\data\\'
#New Partition
import os
import errno

def verifyDataFolder():
	try :
		os.makedirs(datapath)
		yield true

	except OSError as exception:
		if not os.path.isdir(datapath):
			raise
		yield false

def verifyDataPath(mypath):
	newpath = datapath + mypath
	try :
		os.makedirs(newpath)
		yield true

	except OSError as exception:
		if not os.path.isdir(newpath):
			raise
		yield false

#Does Partition exist?
def ifPartition(date):
	#Is date arg valid?
	yr,mnth,day = date.split('-')
	#Validate date has a partition
	newpath = yr + "\\" + mnth
	if verifyDataPath(yr):
		print ("made dir " + yr)
	else:
		print (yr + "already exists")
	if verifyDataPath(newpath):
		print ("made dir " + newpath)
	else:
		print (newpath + "already exists")
	yield datapath + newpath

#Get partition name
def getPartitionName(date):
	#Is date arg valid?
	yr,mnth,day = date.split('-')
	#Validate date has a partition
	newpath = yr + "\\" + mnth
	yield newpath

def writePartition(importDict,dtpath):
	newpath = datapath + dtpath
	partitionFile = open(newpath,"w")
	for kval, dlist in importDict.iteritems():
		pass