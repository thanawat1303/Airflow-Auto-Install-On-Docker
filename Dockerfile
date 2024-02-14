FROM docker:dind

VOLUME [ "/airflow_base" , "/usr/local/bin/dockerd-entrypoint.sh" ]

WORKDIR /airflow_base

EXPOSE 8080