#Mapreduce_training_2
from functools import reduce
from collections import defaultdict
#import datetime

# Define the time window
#start_time = datetime.datetime(2023, 8, 1, 10, 0, 0)
#end_time = datetime.datetime(2023, 8, 1, 10, 40, 0)

# Read data from the provided format
#data = [
 #   "2023-08-01 10:15:23 /page1",
 #   "2023-08-01 10:20:45 /page2",
 #   "2023-08-01 10:30:12 /page1",
 #   "2023-08-01 10:32:56 /page3",
 #   "2023-08-01 10:35:09 /page2"]
with open("access_log.txt","r") as f:
    text = f.readlines()

# Create a defaultdict to count page occurrences
page_counts = defaultdict(int)

# Process data and count occurrences within the time window
for line in text:
    parts = line.split(" ")
    #timestamp = datetime.datetime.strptime(parts[0] + " " + parts[1], '%Y-%m-%d %H:%M:%S')
    #if start_time <= timestamp <= end_time:
    #    page = parts[2]
        page = parts[]
        page_counts[page] += 1

# Display results
for page, count in page_counts.items():
    print(f"Page {page}: {count} occurrences within the time window")
