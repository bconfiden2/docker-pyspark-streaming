export SPARK_MASTER_HOST=`hostname`

bash $SPARK_HOME/sbin/spark-config.sh
bash $SPARK_HOME/bin/load-spark-env.sh

$SPARK_HOME/bin/spark-class org.apache.spark.deploy.master.Master
