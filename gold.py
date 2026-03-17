from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder.getOrCreate()

df = spark.table("dab_demo_silver.data_clean")

result = df.agg(count("*").alias("total_records"))

result.write.mode("overwrite").saveAsTable("dab_demo_gold.metrics")
