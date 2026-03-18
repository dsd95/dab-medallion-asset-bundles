from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.table("dab_demo_bronze.data")
df = df.withColumnRenamed("id", "value")

df.write.mode("overwrite").saveAsTable("medallion_lab.dab_demo_silver.data_clean")
