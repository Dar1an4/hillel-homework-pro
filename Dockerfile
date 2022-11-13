FROM ubuntu:latest
MAINTAINER Alex Pro "alex.pro@alex.pro"
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
RUN make /app
RUN rm -r $HOME/.cache
CMD python3 /app/flask_app/flask_application.py
