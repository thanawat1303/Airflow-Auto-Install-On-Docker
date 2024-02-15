FROM docker:dind

RUN apk add socat

VOLUME [ "/pipeline" ]

COPY ./dockerd-entrypoint.sh /usr/local/bin/dockerd-entrypoint.sh