from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

# Create a SparkSession
spark = SparkSession.builder.appName("AutoIncrement").getOrCreate()

# Create a DataFrame
data = [("John", 30,0), ("Alice", 25,1), ("Bob", 35,2)]
df = spark.createDataFrame(data, ["name", "age","id"])
row=spark.createDataFrame([("Alice", 23456,df.count())],["name", "age"])
df=df.union(row)
row=spark.createDataFrame([("Alice", 23456,df.count())],["name", "age"])
df=df.union(row)
row=spark.createDataFrame([("Alice", 23456,df.count())],["name", "age"])
df=df.union(row)
row=spark.createDataFrame([("Alice", 23456,df.count())],["name", "age"])
df=df.union(row)

# Show the contents of the DataFrame
df.show()