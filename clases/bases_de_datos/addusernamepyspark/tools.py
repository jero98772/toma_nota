import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession.builder.appName('PySpark DataFrame From RDD').getOrCreate()

def writetxt(name,content):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	content =str(content)
	with open(name, 'w') as file:
		file.write(content)
		file.close()

class db:
	def __init__(self,fname):
			self.columns = "id,usr,pwd"
			self.fname = fname
			self.rdd = spark.sparkContext.emptyRDD()
			#self.df=spark.createDataFrame("",self.columns)
	def create(self):
		pass
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	def show(self):
		print(self.df)
class csv(db):
	def __init__(self,fname):
		db.__init__(self,fname)
	def createFile(self):
		writetxt(self.fname,self.columns)
	def readFile(self):
		spark.read.csv(self.fname)