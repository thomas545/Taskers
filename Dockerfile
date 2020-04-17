FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /microworker
WORKDIR /microworker
ADD requirement.txt /microworker/ 
RUN pip install -r requirement.txt 
ADD . /microworker/