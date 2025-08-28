import os
import json
import uuid

import psutil
import time

from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from dotenv import load_dotenv
# for database management use azure-mgmt-cosmosdb


# Load the .env file
load_dotenv()


database_name = "iot"
container_name = "monitoring"
database_endpoint = "https://annafungdba-2025.documents.azure.com:443/"
try:
    print("Hello, Azure CosmosDB!")
    # credential = DefaultAzureCredential()
    # client = CosmosClient(url=database_endpoint, credential=credential)

    # or use connection string
    cosmos_key = os.getenv('COSMOS_KEY')
    client = CosmosClient(url=database_endpoint, credential=cosmos_key)

    database =  client.create_database(database_name) # TODO create database client
    container = database.create_container(container_name)  # TODO create container client
    ID = str(uuid.uuid4())
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    data = [{
        "id": ID,
        "system": "home",  # try to create data for other system, e.g. "work"
        "timestamp": timestamp,
        "cpu_usage": cpu,
        "mem_usage": mem,
    },
    {
       "id": ID,
       "system":"work",
        "timestamp": timestamp,
        "cpu_usage": cpu,
        "mem_usage": mem,
    }]


    print("Creating item...")
    # TODO create the item
    new_item={ 
        "id":"randomstringidnameidontknowwhatthisis",
        "system": "home",
        "timestamp": str( time.time()),
        "cpu_usage":  str(psutil.cpu_percent(1)),
        "mem_usage": str(psutil.virtual_memory())
    }

    # OR QUERY WITH @id parameter (PK)
    print("Querying item...")
    QUERY = "SELECT * FROM c WHERE c.id=@id"   # TODO write the SQL QUERY WITH @id parameter
    SYSTEm="work"
    params = [dict(name="@id", value=ID)]
    # TODO query the container, use parameters, experiment with enable_cross_partition_query flag
    results = container.query_items(
        query=QUERY,
        parameters=params,
        enable_cross_partition_query=True
        )  
    items = [item for item in results]
    output = json.dumps(items, indent=True)
    print("Result list\t", output)


    # Query by system property instead of id (non-PK)
    print("Querying item by system property...")
    QUERY = "SELECT * FROM c WHERE c.system=@system"  # TODO write the SQL QUERY WITH @system parameter aka home.work
    SYSTEM = "home"
    params = [dict(name="@system", value=SYSTEM)]
    #TODO query the container, use parameters, experiment with enable_cross_partition_query flag
    results =  container.query_items(
        query=QUERY,
        parameters=params,
        enable_cross_partition_query=True
        )  

    items = [item for item in results]
    output = json.dumps(items, indent=True)
    print("Result list\t", output)


except Exception as ex:
    print("Exception: ")
    print(ex)
