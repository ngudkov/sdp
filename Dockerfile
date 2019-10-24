# Simple Dockerfile for testing purposes

FROM python:3.6.9-alpine3.10
RUN mkdir -p /opt/test-python
COPY factory_method /opt/test-python/
COPY singletone /opt/test-python/
RUN /opt/test-pyhton/singletone/singletone.py