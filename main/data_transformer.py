from pyspark.sql.functions import col, when, year, month, dayofmonth, from_unixtime, to_date
from pyspark.ml.feature import StringIndexer, StandardScaler, VectorAssembler
from pyspark.ml import Pipeline

def transform_data(df):
    print("Starting data transformation...")
    df = df.withColumn(
        "name", when(col("name") == "", None).otherwise(col("name"))
    ).withColumn(
        "dlc_check", when(col("dlc_count") > 1, 1).otherwise(0)
    ).withColumn(
        "release_date", to_date(from_unixtime(col("release_date") / 1000))
    ).withColumn(
        "release_year", year("release_date")
    ).withColumn(
        "release_month", month("release_date")
    ).withColumn(
        "release_day", dayofmonth("release_date")
    ).drop("release_date")
    
    df = df.dropna(subset=["name", "price", "peak_ccu"])
    print("Data transformation completed.")
    return df

def prepare_data_for_modeling(df):
    print("Preparing data for modeling...")
    categorical_columns = ["genres", "developers", "publishers"]
    numerical_columns = ["price", "dlc_count"]
    
    indexers = [StringIndexer(inputCol=column, outputCol=f"{column}_index") 
                for column in categorical_columns]
    
    assembler = VectorAssembler(
        inputCols=[f"{column}_index" for column in categorical_columns] + numerical_columns,
        outputCol="features"
    )
    
    scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
    pipeline = Pipeline(stages=indexers + [assembler, scaler])
    
    model = pipeline.fit(df)
    df_preprocessed = model.transform(df)
    print("Data preparation for modeling completed.")
    return df_preprocessed
