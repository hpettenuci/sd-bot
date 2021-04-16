FROM python:3.8.6-slim-buster

WORKDIR /usr/src/app

ADD Pipfile* ./

RUN apt-get update  \
    && apt-get install -y --no-install-recommends jq tzdata gcc g++ ca-certificates wget \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -U pipenv && pipenv lock -r > requirements.txt && pip install -r requirements.txt \
    && apt-get remove --purge -y tzdata gcc g++ ca-certificates wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y

COPY src ./

CMD [ "python", "./main.py" ]