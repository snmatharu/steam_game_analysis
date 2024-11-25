import findspark
findspark.init()

from pyspark.sql import SparkSession
import pymongo
import matplotlib.pyplot as plt
import numpy as np

# Test Spark
spark = SparkSession.builder \
    .appName("TestSetup") \
    .getOrCreate()

# Create a simple test DataFrame
test_data = [(1, "test"), (2, "test2")]
test_df = spark.createDataFrame(test_data, ["id", "name"])
test_df.show()

# Test matplotlib
plt.plot([1, 2, 3], [1, 2, 3])
plt.title("Test Plot")
plt.show()

print("All tests completed successfully!")
spark.stop()