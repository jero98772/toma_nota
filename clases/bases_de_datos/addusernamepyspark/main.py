from tools import *
#csvdb=csv("db.csv")
#csvdb.createFile()
NAME="dbs/data.csv"
data=db(NAME)
#data.save_file_csv()
#
try:
	data.read_csv()
except:
	pass
data.show()
data.add_end(("pepe","****"))
data.show()
data.add_end(("pepe2","****"))
data.show()
data.save_file_csv()
