FROM python:3-slim

WORKDIR /usr/src/app

COPY ./src ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]