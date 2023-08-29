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

from pyspark import SparkContext,SparkConf
import re
import time

with open("sales.csv","r") as f:
    text = f.readlines()
    

#Log Analysis