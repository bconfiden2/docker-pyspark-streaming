sudo docker build --force-rm --tag spark-base:3.0.3 ./spark
sudo docker build --force-rm --tag spark-master:3.0.3 ./master
sudo docker build --force-rm --tag spark-worker:3.0.3 ./worker
sudo docker image prune -f

sudo docker-compose up -d

sudo docker exec -d spark-master /opt/spark-3.0.3-bin-hadoop2.7/bin/pyspark --master spark://spark-master:7077
