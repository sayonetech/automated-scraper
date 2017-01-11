############################################################
# Dockerfile for a Scrapy development environment
# Based on Python:2.7 Image
############################################################

FROM python:2.7
MAINTAINER jithin.sayone@gmail.com

RUN apt-get update


#Add folder to docker
ADD . /home/auto-scraper-website

#install dependencies
RUN pip install -r /home/auto-scraper-website/requirements.txt

COPY start_crawl.py /cmd/start_crawl.py

ENTRYPOINT  python /cmd/start_crawl.py
