FROM python:3.11-alpine

RUN apk add git openssh

RUN mkdir -p /root/.ssh
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
RUN touch /root/.ssh/known_host
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN git clone git@github.com:nicolausmg/assignment3.git .

RUN pip install flask

CMD ["python", "web.py"]

