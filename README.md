# ElasticSearch-Log-Analysis

# Requriements
Requires a Machine with at least 8GB of RAM

# Configure WSL2 to use max only 4GB of ram
```
wsl --shutdown
notepad "$env:USERPROFILE/.wslconfig"
```
.wslconfig file:
```
[wsl2]
memory=4GB   # Limits VM memory in WSL 2 up to 4GB
```

## Enter in WSL before Start
sudo sysctl -w vm.max_map_count=262144

# Kibana
SELECT * FROM "etl_monitori*" WHERE date = '2022-03-02'

# Logging
1 Execute 01 to create index
2 go in Kibana :5601 and Stack management
2.1 in index management show new index 
2.2 click on it to see the mapping
3 go to index patterns and create new index pattern for etl monitoring
4 execute 04 to bring in data
5 go to discover and show that the data is in
6 create a dashboard
7 create a visualization (use TSVB)
8 go back to discover and search for status error - see the error 


