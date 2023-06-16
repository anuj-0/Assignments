# USING LATEST POSTGRES IMAGE
FROM postgres:latest 

# SWITCH TO ROOT USER
USER root

# STEPS TO BUILD PYTHON VERSION 3.7
RUN apt-get -y update
RUN apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
RUN wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
RUN tar -xf Python-3.7.12.tgz
WORKDIR /Python-3.7.12
RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall

# STEPS TO INSTALL AIRFLOW VERSION 2.5.0
RUN apt-get install libpq-dev
RUN pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"