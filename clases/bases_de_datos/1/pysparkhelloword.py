import pyspark
spark = pyspark.sql.SparkSession.builder.appName('PySpark Read CSV').getOrCreate()
df = spark.read.options(header=True,inferSchema=True).csv("data1.csv")
print(df.count())
print(df.printSchema())
cols=["id","usr","pwd"]
dftmp=spark.createDataFrame([(1,"gg","secret")],cols)
newdf=df.union(dftmp)
newdf.write.csv("data1.csv")