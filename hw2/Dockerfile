FROM python:3.8-slim

WORKDIR /hw2

RUN apt-get update -y
RUN apt-get install -y iputils-ping

COPY main.py .

ENTRYPOINT ["python", "-m", "main"]