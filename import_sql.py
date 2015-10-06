#SQL for importer
datapath = 'C:\\Users\\djwilli\\Documents\\Programs\\data\\'
#New Partition
def createMaster()
	#STB|TITLE|PROVIDER|DATE|REV|VIEW_TIME

	"CREATE TABLE viewtrakmstr (
    set_top_id      int not null,
    view_title      char,
    logdate         date not null,
    revenue         float
	)"

def createPartition(date)
	createMaster()
	pass

#Does Partition exist?
def ifPartition(date)
	#Is date arg valid?
	yr,mnth,day = date.split('-')
	#Validate date has a partition

	pass

#Get partition name
def getPartitionName(date)
	pass
	