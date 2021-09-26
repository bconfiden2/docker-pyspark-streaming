FROM spark-base:3.0.3

COPY start-master.sh /

RUN apt-get install -y python3-pip
RUN pip3 install jupyter
RUN apt-get install -y netcat
RUN pip3 install tweepy
RUN mkdir /notebooks

EXPOSE 8080 7077 8888 4040

CMD ["/bin/bash", "/start-master.sh"] 
