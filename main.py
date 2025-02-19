import os
import json
import uuid

import psutil
import time

from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient

# for database management use azure-mgmt-cosmosdb

database_name = "iot"
container_name = "monitoring"
database_endpoint = "https://mdsummer2025.documents.azure.com:443/"
try:
    print("Hello, Azure CosmosDB!")
    # credential = DefaultAzureCredential()
    # client = CosmosClient(url=database_endpoint, credential=credential)

    # or use connection string
    cosmos_key = os.getenv('COSMOS_KEY')
    client = CosmosClient(url=database_endpoint, credential=cosmos_key)

    database = None  # TODO create database client
    container = None  # TODO create container client
    ID = str(uuid.uuid4())
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    data = {
        "id": ID,
        "system": "home",  # try to create data for other system, e.g. "work"
        "timestamp": timestamp,
        "cpu_usage": cpu,
        "mem_usage": mem,
    }

    print("Creating item...")
    # TODO create the item

    # OR QUERY WITH @id parameter (PK)
    print("Querying item...")
    QUERY = None  # TODO write the SQL QUERY WITH @id parameter
    params = [dict(name="@id", value=ID)]
    results = None  # TODO query the container, use parameters, experiment with enable_cross_partition_query flag

    items = [item for item in results]
    output = json.dumps(items, indent=True)
    print("Result list\t", output)


    # Query by system property instead of id (non-PK)
    print("Querying item by system property...")
    QUERY = None  # TODO write the SQL QUERY WITH @system parameter
    SYSTEM = "home"
    params = [dict(name="@system", value=SYSTEM)]
    results = None  # TODO query the container, use parameters, experiment with enable_cross_partition_query flag

    items = [item for item in results]
    output = json.dumps(items, indent=True)
    print("Result list\t", output)


except Exception as ex:
    print("Exception: ")
    print(ex)
