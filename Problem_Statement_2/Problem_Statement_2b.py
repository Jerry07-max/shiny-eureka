import re
from collections import Counter

# Creation of log file to analyze
Log_file = 'access.log'

# Regular expressions to match log components
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(?P<method>\w+) (?P<page>.*?) HTTP/.*?" (?P<status>\d+)')

# Initializing Counters
ip_counter = Counter()
page_counter = Counter()
error_404_count = 0

# Analyzing the log file
with open(Log_file, 'r') as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            data = match.groupdict()
            ip_counter[data['ip']] += 1
            page_counter[data['page']] += 1
            if data['status'] == '404':
                error_404_count += 1

# Creation of Summarized report
print(f"Total 404 errors: {error_404_count}")
print("\nTop 5 most requested pages:")
for page, count in page_counter.most_common(5):
    print(f"{page}: {count} requests")

print("\nTop 5 IP addresses with most requests:")
for ip, count in ip_counter.most_common(5):
    print(f"{ip}: {count} requests")
