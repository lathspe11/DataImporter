#python importer.py 
import import_sql
import csv 
import sys
import os
import getopt

errlog = 'C:\\Users\\djwilli\\programs\\data\\importerrors.txt'
importFile = import_sql.datapath + 'initdata.txt'

def usageMsg():
	print("you're doing it wrong.")

headers = list()
linedata = list()
partdict = {}
vuedict = {}

#Read the import file and merge with the proper data store files
#I'm assuming the data is validated and I'm not doing typical checks 
def readImport(openme):
	with open(openme, 'r') as todayfile:
		readOneLine = csv.reader(todayfile, delimiter='|',quotechar='"')

		#Strip off the header
		headers = next(readOneLine)
		print(headers[0:])

		for aline in readOneLine:
			key = aline[0] + '|' + aline[1] + '|' + aline[3]
			yr,mnth,day = aline[3].split('-')
			partnam = yr+"\\"+mnth
			#Collect the date values to use as partition
			if partnam in partdict.keys():
				#print("add to %s" % partnam)
				partdict[partnam] += 1
			else:
				#print("init partition %s" % partnam)
				partdict[partnam] = 1
				ppath = import_sql.ifPartition(aline[3])
			print(key + " %s" % ' '.join(str(x) for x in aline))
			vuedict[key] = aline

		#print("number of viewings " + str(len(vuedict)))
		#print("number of partitions " + str(len(partdict)))
		
		#for each partition open the stored list
		#Merge the current list with stored list
		#allDicts = {}
		#look at each partition in order
		mysortlist = sorted(partdict.keys())
		for dtpath in mysortlist:
			#Get the data store 
			dsdict = import_sql.openPartition(dtpath)
			#allDicts.update(dsdict)
			dsdict.update(vuedict)
			#write the data for that store
			import_sql.writePartition(dsdict,dtpath)
		#Update the stores 
		#Write the combined data to storage
		#allDict.update(vuedict)
		#import_sql.writePartition(allDict,dtpath)
		
def main():
	#Collect and parse the args
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hs")
	
	print('Program Completed')

if __name__ == "__main__":
	main()
