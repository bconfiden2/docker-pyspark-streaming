# docker-spark-cluster

Run Spark Cluster for Stream Processing, with using
- pyspark (driver=jupyter notebook)
- dockerfile
- docker-compose

<br>

### Run
```
cd REPO_DIR
bash start-cluster.sh
```

If it is the first run, it takes time to create an docker image.

You might see weird red texts that looks like an error message, but it's just a process of downloading a file.

After master/worker containers are made, you can access the pyspark running on the cluster, from ```localhost:8888```.

Some notebook files(.ipynb) are in ```/notebooks``` directory in master container, and it is connected with ```REPO_DIR/codes``` directory of HostOS, by docker volume.

<br>

### Stop
```
bash stop-cluster.sh
```
