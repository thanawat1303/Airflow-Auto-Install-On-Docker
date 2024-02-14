FROM docker:dind

VOLUME [ "/airflow_base" , "/usr/local/bin/dockerd-entrypoint.sh" ]

WORKDIR /airflow_base

RUN mkdir /airflow_base/config /airflow_base/logs /airflow_base/plugins

EXPOSE 8080