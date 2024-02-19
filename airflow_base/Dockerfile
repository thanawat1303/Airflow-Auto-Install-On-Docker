FROM apache/airflow:2.8.1

VOLUME ["/opt/airflow/pipe" , "/var/run/docker.sock" ]

ADD requirements.txt .
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt