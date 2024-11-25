from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType, LongType

def fetch_data_with_pymongo():
    print("Fetching data from MongoDB...")
    from config import get_mongo_url
    
    mongo_url = get_mongo_url()
    client = MongoClient(mongo_url)
    db = client["steam"]
    collection = db["games"]
    
    def convert_bson_types(record):
        record["_id"] = str(record["_id"])
        if "release_date" in record:
            record["release_date"] = int(record["release_date"])
        return record

    choice = input("Enter 0 to fetch all records or 1 to fetch 5000 records: ")
    
    if choice == "0":
        print("Fetching all records from MongoDB.")
        data = [convert_bson_types(record) for record in collection.find()]
    else:
        print("Fetching 5000 records from MongoDB.")
        data = [convert_bson_types(record) for record in collection.find().limit(5000)]
    
    client.close()
    print(f"Fetched {len(data)} records from MongoDB.")
    return data

def get_schema():
    return StructType([
        StructField("_id", StringType(), True),
        StructField("name", StringType(), True),
        StructField("detailed_description", StringType(), True),
        StructField("price", FloatType(), True),
        StructField("dlc_count", LongType(), True),
        StructField("release_date", LongType(), True),
        StructField("genres", StringType(), True),
        StructField("developers", StringType(), True),
        StructField("publishers", StringType(), True),
        StructField("peak_ccu", LongType(), True)
    ])

def create_spark_session():
    print("Initializing Spark session...")
    spark = SparkSession.builder \
        .appName("MongoDBIntegration") \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.executor.memory", "4g") \
        .config("spark.driver.memory", "4g") \
        .getOrCreate()
    print("Spark session initialized.")
    return spark

def convert_to_spark_dataframe(spark, data):
    print("Converting pymongo data to PySpark DataFrame...")
    schema = get_schema()
    df = spark.createDataFrame(data, schema=schema)
    print("Data successfully converted to PySpark DataFrame.")
    return df
