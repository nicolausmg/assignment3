FROM python:3.11-alpine
 
RUN apk add --no-cache git openssh
 
RUN mkdir -p /root/.ssh
ADD id_rsa_key /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan -H github.com >> /root/.ssh/known_hosts
 
RUN git clone git@github.com:nicolausmg/assignment3.git /app
 
WORKDIR /app/web_service
 
RUN pip install flask
 
CMD ["python", "web.py"]
