import csv
from datetime import datetime
import os

log_file = "logs/logs.csv"

# Create file if not exists
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "query", "intent", "distance"])

def log_query(query, intent, distance):
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), query, intent, distance])