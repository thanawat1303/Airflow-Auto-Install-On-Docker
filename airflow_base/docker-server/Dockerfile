FROM docker:dind

RUN apk add socat && socat TCP4-LISTEN:2375,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock &

VOLUME [ "/pipeline/data" , "/pipeline/task" ]