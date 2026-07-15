from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="taxi_trips.csv")
parser.add_argument("--output", default="results.parquet")
args = parser.parse_args()

spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()

df = spark.read.option("header", True).csv(args.input)

clean = df.filter(col("fare_amount").isNotNull() & (col("fare_amount") > 0))
agg = (
    clean.groupBy("passenger_count")
    .agg(avg("fare_amount").alias("avg_fare"), count("*").alias("trips"))
)

agg.write.mode("overwrite").parquet(args.output)
print("Aggregation saved to", args.output)
spark.stop()
