FROM docker:dind

RUN apk add socat

VOLUME [ "/airflow_base/pipe" ]

COPY ./dockerd-entrypoint.sh /usr/local/bin/dockerd-entrypoint.sh