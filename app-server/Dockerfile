############################################################
# Dockerfile for a Django development environment
# Based on Python:2.7 Image
############################################################

FROM python:2.7
MAINTAINER jithin.sayone@gmail.com

RUN apt-get update

#Add Project to docker
ADD . /app/

#Install dependencies
RUN pip install -r /app/requirements.txt
 
CMD python /app/manage.py makemigrations && \
    python /app/manage.py migrate && \
    python /app/manage.py create && \
    python /app/manage.py data && \
    python /app/manage.py collectstatic --noinput && \
    python /app/manage.py runserver 0.0.0.0:8000 
    
    
