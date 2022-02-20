From ubuntu:20.04

ENV SPARK_HOME=/opt/spark-3.0.3-bin-hadoop2.7
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
ENV	PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y wget
RUN apt-get install -y python3
RUN wget https://archive.apache.org/dist/spark/spark-3.0.3/spark-3.0.3-bin-hadoop2.7.tgz && tar -xzf spark*.tgz && rm spark*.tgz && mv spark* /opt
RUN mkdir /data

CMD ["/bin/bash"]
