FROM tiangolo/uwsgi-nginx-flask:python3.6

ARG ENV
ENV ENV ${ENV}

RUN apt-get update
RUN apt-get -y install default-libmysqlclient-dev || apt-get -y install libmysqlclient-dev

ADD ./requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip install -r requirements.txt

COPY app /backend/app
COPY templates /backend/templates
COPY run.py /backend/run.py
COPY run.sh /backend/run.sh


RUN chmod +x /backend/run.sh

#CMD python database.py

CMD ./run.sh