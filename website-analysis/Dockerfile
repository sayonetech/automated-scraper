############################################################
# Dockerfile for a Scrapy development environment
# Based on Python:2.7 Image
############################################################

FROM python:2.7
MAINTAINER jithin.sayone@gmail.com

RUN apt-get update



#install requirement packages
RUN pip install attrs==15.2.0
RUN pip install cffi==1.6.0
RUN pip install cryptography==1.3.2
RUN pip install cssselect==0.9.1
RUN pip install lxml==3.6.0
RUN pip install parsel==1.0.2
RUN pip install pyasn1-modules==0.0.8
RUN pip install PyDispatcher==2.0.5
RUN pip install pyOpenSSL==16.0.0
RUN pip install PyYAML==3.11
RUN pip install queuelib==1.4.2
RUN pip install requests==2.10.0
RUN pip install Scrapy==1.2.0
RUN pip install selenium==2.53.2
RUN pip install Twisted==16.2.0
RUN pip install zope.interface==4.1.3
RUN pip install translate
RUN pip install psycopg2==2.6.2
RUN pip install bs4==0.0.1
RUN pip install requests-cache==0.4.12
RUN pip install pybloom==1.1



#Add folder to docker
ADD . /home/auto-scraper-website

COPY start_crawl.py /cmd/start_crawl.py




ENTRYPOINT  python /cmd/start_crawl.py

