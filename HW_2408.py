<<<<<<< HEAD
from functools import reduce
from collections import defaultdict
import datetime

## MapReduce tasks
# 1) URL Access Count:
with open("access_log.txt", "r") as f:
    text = f.readlines()

page_counts = defaultdict(int)

for line in text:
    parts = line.split(" ")
    page = parts[2]
    page_counts[page] += 1

for page, count in page_counts.items():
    print(f"Page {page}: {count} occurrences within the time window")

# # 2)Follower Recommendations
# with open("follower_graph.txt", "r") as f:
#     text = f.readlines()


## Spark Tasks
# Data Aggregation

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("TotalAmount").getOrCreate()

data = spark.read.options(delimiter=",").csv("sales.csv", header=True, inferSchema=True)
average_scores = data.groupBy("Category").agg(sum("Amount").alias("TotalAmount"))

average_scores.show()
spark.stop()

# Log Analysis
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("LogAnalysis")
sc = SparkContext(conf=conf)

lines = sc.textFile("server_log.txt")


def parse_log(line):
    web, ip = line.split(" ")
    return (web, ip)


sorted_web = (
    lines.flatMap(lambda line: line.split())
    .map(parse_log)
    .reduceByKey(lambda a, b: a + b)
)

for web, count in sorted_web:
    print(f"URL: {web}, Access Count: {ip}")

sc.stop()
=======
from functools import reduce
from collections import defaultdict
import datetime

#MapReduce
#1) URL Access Count:
with open("access_log.txt","r") as f:
    text = f.readlines()

page_counts = defaultdict(int)

for line in text:
    parts = line.split(" ")
    page = parts[2]
    page_counts[page] += 1

for page, count in page_counts.items():
    print(f"Page {page}: {count} occurrences within the time window")

#2)Follower Recommendations
with open("follower_graph.txt","r") as f:
    text = f.readlines()


#Spark Tasks
#Data Aggregation

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("TotalAmount").getOrCreate()

data = spark.read.options(delimiter=",").csv("sales.csv", header=True, inferSchema=True)
average_scores = data.groupBy("Category").agg(sum("Amount").alias("TotalAmount"))

average_scores.show()
spark.stop()

#Log Analysis
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("LogAnalysis")
sc = SparkContext(conf=conf)

lines = sc.textFile("server_log.txt")


def parse_log(line):
    web, ip = line.split(" ")
    return (web, ip)


sorted_web = (
    lines.flatMap(lambda line: line.split())
    .map(parse_log)
    .reduceByKey(lambda a, b: a + b)
)

for web, count in sorted_web:
    print(f"URL: {web}, Access Count: {ip}")

sc.stop()
>>>>>>> aa525cd710b83107ae6e676dbb4345ac3e36c0f4
