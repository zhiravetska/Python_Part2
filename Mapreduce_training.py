#from functools import reduce
#from collections import defaultdict

# Sample datapip 
#data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map function
#def map_function(item):
    #return (item % 2, item) # Group even and odd numbers

# Reduce function
#def reduce_function(key, values):
    #return key, sum(values)

# Map stage
#mapped_data = map(map_function, data)

# Shuffle and Sort (group by key)
#intermediate = defaultdict(list)
#for key, value in mapped_data:
    #intermediate[key].append(value)

# Reduce stage
#final_result = []
#for item in intermediate.items():
    #result = reduce(reduce_function, item)
    #final_result.append(result)
#print(final_result)

from functools import reduce
from collections import defaultdict
import datetime

# Define the time window
start_time = datetime.datetime(2023, 8, 1, 10, 0, 0)
end_time = datetime.datetime(2023, 8, 1, 10, 40, 0)

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
    timestamp = datetime.datetime.strptime(parts[0] + " " + parts[1], '%Y-%m-%d %H:%M:%S')
    if start_time <= timestamp <= end_time:
        page = parts[2]
        page_counts[page] += 1

# Display results
for page, count in page_counts.items():
    print(f"Page {page}: {count} occurrences within the time window")