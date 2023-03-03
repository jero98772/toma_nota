import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.types import StructType, StructField, IntegerType, StringType


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
			self.columns = "usr,pwd"
			"""self.schema = StructType([
				StructField("id", IntegerType(), True),
				StructField("usr", StringType(), True),
				StructField("pwd", StringType(), True)
				])"""
			self.schema = "id INT,usr STRING,pwd STRING"
			self.fname = fname
			self.rdd = spark.sparkContext.emptyRDD()

			self.df=spark.createDataFrame([],self.schema)

	def show(self):
		self.df.show()
	def read_csv(self):#work
		self.df=spark.read.csv(self.fname, header=True, inferSchema=True)
	def save_file_csv(self):#
		#self.df.write.format("csv").mode("overwrite").option("header", "true").save(self.fname)
		spark.catalog.refreshByPath(self.fname)
		self.df.coalesce(1).write.mode('overwrite').option("header", "true").csv(self.fname)


		#self.df.write.format("csv").option("header", True).mode("overwrite").save(self.fname)
	def add_end(self,data:tuple):
		row=spark.createDataFrame([(self.df.count(),data[0],data[1])],self.schema)
		self.df=self.df.union(row)
	#def remove(self,id):
	
