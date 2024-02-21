FROM apache/airflow:2.8.1

VOLUME ["/airflow_base/Data" , "/var/run/docker.sock" ]

ADD requirements.txt .
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
ENV PYTHONPATH="/opt/airflow/dags/Python"