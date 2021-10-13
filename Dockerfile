FROM python:3.8.6-alpine3.12
WORKDIR /src
ADD factorial.py /src
CMD python3 ./factorial.py
    