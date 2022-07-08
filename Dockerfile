FROM rhel7
RUN yum install -y python python-pip
RUN yum install -y python36 

RUN pip3 install

COPY app.py /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
