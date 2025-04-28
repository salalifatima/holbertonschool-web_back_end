#!/usr/bin/env python3

from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Count total logs
    total_logs = collection.count_documents({})

    # Count methods
    methods_count = {
        "GET": collection.count_documents({"method": "GET"}),
        "POST": collection.count_documents({"method": "POST"}),
        "PUT": collection.count_documents({"method": "PUT"}),
        "PATCH": collection.count_documents({"method": "PATCH"}),
        "DELETE": collection.count_documents({"method": "DELETE"}),
    }

    # Count GET requests to /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: {methods_count[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
