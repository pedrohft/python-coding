from pyspark.sql import SparkSession
import pandas

spark = SparkSession.builder.appName("Test").getOrCreate()

pdf = pandas.read_excel('excelfile.xlsx', sheet_name='sheetname', inferSchema='true')
df = spark.createDataFrame(pdf)

df.show()