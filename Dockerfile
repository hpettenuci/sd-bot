FROM python:3-alpine

RUN apk update --no-cache \
    && apk add  git gcc g++ curl \
    && rm -rf /tmp/* /var/tmp/*

WORKDIR /usr/src/app

COPY src ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]