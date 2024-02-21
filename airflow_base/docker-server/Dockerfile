FROM docker:dind

RUN apk add socat

VOLUME [ "/airflow_base/Data" , "/airflow_base/dags/Docker" ]

COPY ./dockerd-entrypoint.sh /usr/local/bin/dockerd-entrypoint.sh