#!/bin/zsh

# create the database account
az cosmosdb create --name mdsummer2025 --kind GlobalDocumentDB --resource-group DataAcademySummer2025

# list accounts (shows document endpoint uri)
az cosmosdb list -g DataAcademySummer2025 -o table

# create the database
az cosmosdb sql database create --account-name mdsummer2025 --name "iot" --resource-group DataAcademySummer2025

# create the container
az cosmosdb sql container create --account-name mdsummer2025 --database-name "iot" --name "monitoring" --partition-key-path "/id" --throughput 400 --resource-group DataAcademySummer2025

# show the database keys
az cosmosdb keys list --name mdsummer2025 --resource-group DataAcademySummer2025

# show the database connection strings
az cosmosdb keys list --type connection-strings --name mdsummer2025 --resource-group DataAcademySummer2025