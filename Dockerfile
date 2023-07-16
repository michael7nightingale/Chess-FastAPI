FROM python:3.11


COPY server ./server

WORKDIR ./server

RUN pip install -r /server/server-requirements.txt
