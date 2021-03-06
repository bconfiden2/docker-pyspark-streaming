# docker-pyspark-streaming-cluster

Run Spark Cluster for Stream Processing, with using
- pyspark (driver=jupyter notebook)
- dockerfile
- docker-compose

### Run
```
cd [REPOSITORY]
sudo apt-get install -y docker-compose
bash start-cluster.sh
```

If it is the first run, it takes time to create an docker image.

You might see weird red texts that looks like an error message, but it's just a process of downloading a file.

After master/worker containers are made, you can access the pyspark running on the cluster, from ```localhost:8889```.

Some notebook files(.ipynb) are in ```/notebooks``` directory in master container, and it is connected with ```REPO_DIR/codes``` directory of HostOS, by docker volume.

### Stop
```
bash stop-cluster.sh
```
