#!/usr/bin/env python3
"""
Modul for task 12:
Write a Python script that provides some stats about
Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip
The output of your script must be exactly the same as the example
"""
from pymongo import MongoClient


def log_stats():
    """returns the list of school having a specific topic"""
    client = MongoClient("mongodb://localhost:27017/")
    logs = client.logs.nginx.count_documents({})
    print(f"{logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = client.logs.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status = client.logs.nginx.count_documents({"method": "GET", "path":
                                                "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
