from pyspark.sql import SparkSession

spark = SparkSession.builder \
          .appName("PySparkTest") \
          .getOrCreate()

data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()