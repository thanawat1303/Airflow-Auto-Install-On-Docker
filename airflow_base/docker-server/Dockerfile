FROM docker:dind

RUN apk add socat

VOLUME [ "/pipe" ]

COPY ./dockerd-entrypoint.sh /usr/local/bin/dockerd-entrypoint.sh