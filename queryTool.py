import argparse
import import_sql
import operator

#print(dir(argparse.ArgumentParser))
mydate = '2014-04-01'
colDict = {'STB':0,'TITLE':1,'PROVIDER':2,'DATE':3,'REV':4,'VIEW_TIME':5}
vuedict = {}
vuelist = []

def selectcolum(colStr):
	listCols = list()
	transCols = list()
	listCols = colStr.split(',')
	for aCol in listCols:
		ucCol = aCol.upper()
		if ucCol in colDict:
			transCols.append(colDict[ucCol]) 
		else:
			print("Did not find select string %s" % aCol)
	return transCols

#Filter data remove all but what matches the column value
def filtercolum(colStr):
	listCols = list()
	transCols = list()
	aCol,value = colStr.split('=')
	ucCol = aCol.upper()
	if ucCol in colDict:
		tCol = colDict[ucCol]
	else:
		print("Did not find filter string %s" % aCol)
	return tCol,value

def main():
	argparse.ArgumentParser
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-s', action="store", dest="select", 
	help='select columns to display')
	parser.add_argument('-o', action="store", dest="order", 
	help='order by columns')
	parser.add_argument('-f', action="store", dest="filter", help='filter data with a column value')
	parser.add_argument('-g', action="store", dest="group", help='Group columns to display')

	args = parser.parse_args()

	#print(vars(args)) 
	#Open the list 
	apath = import_sql.getPartitionName(mydate)
	vuedict = import_sql.openPartition(apath)
	if args.filter != None:
		print(args.filter)
		aCol,aVal = filtercolum(args.filter)
		print(aCol , aVal)
		for v in vuedict.values():
			if v[aCol] == aVal:
				vuelist.append(v)
	else:
		for v in vuedict.values():
			vuelist.append(v)
	
	#vuelist has all records I want
	#Sort the vuelist if required
	if args.order != None:
		olist = selectcolum(args.order)
		#we will apply the sort in reverse order
		olist.reverse()
		newlist = list()
		#for each indicies in olist sort my list
		#Failed #newlist = sorted(vuelist,key=operator.itemgetter(','.split(olist)))
		for dx in olist:
			vuelist.sort(key=lambda x: x[dx])
	
	#select display columns
	if args.select != None:
		clist = sorted(selectcolum(args.select))
		newlist = list()
		for v in vuelist:
			showlist = list()
			for c in clist:
				showlist.append(v[c])
			newlist.append(showlist)
	#order columns
	for ln in newlist:
		nustr = "'%s" % "', '".join(ln)
		print(nustr + "'")

	
main()
