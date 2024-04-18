#!/usr/bin/env python
# coding: utf-8

import argparse
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

# Define the parser
parser = argparse.ArgumentParser()
parser.add_argument('--input_sp500', required=True,
                    help='Input file path for S&P 500 data.')
parser.add_argument('--output', required=True,
                    help='Output table name for BigQuery.')

args = parser.parse_args()

input_sp500 = args.input_sp500
output = args.output

# Create Spark session
spark = SparkSession.builder \
    .appName('SP500 Volume Analysis') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket',
               'dataproc-us-central')

# Define schema for S&P 500 data for csv file option
sp500_schema = StructType([
    StructField("Date", StringType(), True),
    StructField("Symbol", StringType(), True),
    StructField("Adj Close", DoubleType(), True),
    StructField("Close", DoubleType(), True),
    StructField("High", DoubleType(), True),
    StructField("Low", DoubleType(), True),
    StructField("Open", DoubleType(), True),
    StructField("Volume", LongType(), True)
])

# Load S&P 500 data
# Load S&P 500 data from a Parquet file
df_sp500 = spark.read.parquet(input_sp500)


# Calculate the top 5 companies by volume
top5_volume = df_sp500.groupBy('Symbol').agg(F.sum('Volume').alias(
    'TotalVolume')).orderBy(F.desc('TotalVolume')).limit(5)

# Display top 5 results (optional, remove in production)
top5_volume.show()

# Save the top 5 results to BigQuery
top5_volume.write.format('bigquery') \
    .option('table', output) \
    .save()
