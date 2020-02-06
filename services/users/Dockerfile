FROM python:3.7.2-slim

RUN apt-get update && \
 apt-get -y install netcat && \
 apt-get clean

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/scr/app/entrypoint.sh

COPY . /usr/src/app
CMD ["/usr/src/app/entrypoint.sh"]
