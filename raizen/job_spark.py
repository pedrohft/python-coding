from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Ler os dados do enem 2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-pedroteixeira-763282822520-producao/raw/")
)


(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-pedroteixeira-763282822520-producao/staging/docentes/")
)