import pyspark as pd
import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = SparkSession.builder \
          .appName("PySparkTest") \
          .getOrCreate()

data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]

# Create a pandas-on-Spark DataFrame
df = ps.DataFrame({'id': [1, 2, 3], 'value': ['a', 'b', 'c']})
df = spark.createDataFrame(data, ["Name", "Age"])


# Perform operations as you would with pandas
print(df.head())
df.show()