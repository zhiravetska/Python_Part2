from pyspark import SparkConf, SparkContext

# from pyspark.sql import SparkSession

# Initialize Spark session
# sc = SparkSession.builder.appName("LogAnalysis").getOrCreate()
conf = SparkConf().setAppName("LogAnalysis")
sc = SparkContext(conf=conf)

# Sample data
# data = [
#     ("2023-08-01 10:15:23", "/page1", "192.168.1.100"),
#     ("2023-08-01 10:20:45", "/page2", "192.168.1.101"),
#     ("2023-08-01 10:30:12", "/page1", "192.168.1.102"),
#     ("2023-08-01 10:32:56", "/page3", "192.168.1.100"),
#     ("2023-08-01 10:35:09", "/page2", "192.168.1.103"),
# ]

# Create an RDD
# data = sc.read.options(delimiter=",").csv(
#    "server_log.txt", header=True, inferSchema=True
# )
lines = sc.textFile("server_log.txt")


# Define a function to parse the log data
def parse_log(line):
    web, ip = line.split(" ")
    return (web, ip)


# Map the data and perform aggregation
# url_ip_rdd = rdd.map(parse_log)
# url_counts = url_ip_rdd.countByKey()
sorted_web = (
    lines.flatMap(lambda line: line.split())
    .map(parse_log)
    .reduceByKey(lambda a, b: a + b)
)

# Find the most frequently accessed URLs
# sorted_urls = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)

# Display the results
for web, count in sorted_web:
    print(f"URL: {web}, Access Count: {ip}")

# Close the Spark session
sc.stop()

# spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()

# conf = SparkConf().setAppName("LogAnalysis")
# sc = SparkContext(conf=conf)

# lines = sc.textFile("server_log.txt")

# # start_time = time.time()
# # word_counts = lines.flatMap(lambda line:line.split()).map(map_word).reduceByKey(lambda a,b:a+b)
# sorted_urls = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)

# with open("server_log.txt", "w") as f:
#     for word, count in word_counts.collect():
#         f.write(str((word, count)) + "\n")

# # result_time = time.time() - start_time#4.2850182056427
# print("Result time : " + str(result_time))
# sc.stop()
