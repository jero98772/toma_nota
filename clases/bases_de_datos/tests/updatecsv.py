from pyspark.sql import SparkSession
import pandas as pd
spark = SparkSession.builder.appName("update-csv").getOrCreate()
p="test.csv"
schema = ["null","name","age","id"]#"id INT,usr STRING,pwd STRING"

df = spark.read.csv(p, header=True)
print(df)
row=spark.createDataFrame([("Alice", 23456,df.count())])
df=df.union(row)
row=spark.createDataFrame([("Alice", 23456,df.count())])
df=df.union(row)
row=spark.createDataFrame([("Alice", 23456,df.count())])
df=df.union(row)
row=spark.createDataFrame([("Alice", 23456,df.count())])
df=df.union(row)

print(df)

pandasDF = df.toPandas()
pandasDF.to_csv(p,sep=",",index=False)
