FROM python:3.7.4-alpine

LABEL Tige Phillips <tige@ignw.io>


# PYTHON and TOOLS
###################
RUN apk update
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk add --no-cache bash
RUN pip3 install --upgrade pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt 

RUN apk add libffi-dev openssl-dev python3-dev
# RUN apk add gcc

# RUN apk add git
# RUN apk add musl-dev
# RUN apk add linux-headers

WORKDIR /root
COPY cloudcenter_deploy.py ./
COPY settings.py ./
COPY settings.yaml ./
COPY restful.json ./


