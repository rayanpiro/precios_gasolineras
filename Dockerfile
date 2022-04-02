FROM python:3.10.4-alpine3.14

RUN apk add curl

WORKDIR /usr/src/app

COPY app/requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY entrypoint.sh /
COPY renew_data /etc/periodic/15min

RUN chmod +x /entrypoint.sh /etc/periodic/15min/*

COPY app/ .

ENTRYPOINT [ "/entrypoint.sh" ]