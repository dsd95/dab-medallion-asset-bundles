from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.range(1000)

df.write.mode("overwrite").saveAsTable("medallion_lab.dab_demo_bronze.data")
