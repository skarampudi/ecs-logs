FROM ubuntu:20.04
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python3
WORKDIR /opt/python
COPY ./app.py .
EXPOSE 8000
ENTRYPOINT ["python3", "/opt/python/app.py"]
