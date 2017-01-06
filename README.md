The project consist of two parts :
1)A Scrapy project- which is used to crawl particular set of data from specified url list.
2)A Django REST API-which is used to access the result of the scraped data,and shows it to users.

To see furthur details of the working system, please refer ``` spec ``` folder in repo

## Run locally

1. Clone the project

```
git clone 
cd sme-website-scraper
```

###install Docker
1. Get the latest Docker package

   ```    
        sudo apt-get install docker docker.io
        sudo apt-get install docker docker-engine 
   ```
       or

      ```  sudo apt-get install docker docker-machine ```
2. Add yourself to the docker group, log out, and then login back to ensure that you can run Docker commands without sudo:
 	``` sudo usermod -a -G docker $USER ```

3. Verify docker is installed correctly
      ``` sudo docker run hello-world ```

###System Overview

In our system there are 3 containers which work together to make our system scalable with any number of urls
1.DataBase
2.Appserver
3.Scraper


###DB Container 
This container holds the DB for the use of our system.The container is build on the base image of Postgres(i.e postgres:9.4).The ENV_variables which should be passed are :
- POSTGRES_PASSWORD:Password of database user
- POSTGRES_USER:Username of the database ,who have privilage to use
- POSTGRES_DB: Datatabase name in which the table will be created
For persisted use of DB data after it restarts, we will mount a volume, so data will not be lost.The path to which we mount will be '/var/lib/postgresql/data'

### Scraper Container 
 This container hold the scraper i.e the container which will crawl the list of url and save that to the Database.The Dockerfile for the docker image will be present in the repo under web-analysis folder.The ENV_varables which should be passed are:
- DB_PASSWORD:Password for the DB user name .
- DB_USER:User name of the DB which have the privilage to use the data.
- DB_NAME: Database name which is defined in Db container
- DB_HOST: The ip in which the DB container is hosted(since we made links, we need to give only the DB conatiner name)

Since our container is in a network, we have to link them.Scraper container will be linked to DB container and Appserver container. We are using Docker compose to rebuild same on local. And for caching the response of the url request, we have to mount a volume in the path '/scraper-cache',so the cached data will not be lost. We can reuse the data once we restart the container.

###Appserver Container 

This container will hold the Appserver,ie, API service for our scraper.The data which is saved in DB by scraper can be accessed using this container.The Dockerfile for the docker image will be present in the repo under'app-server' folder.The ENV_variables  which should be passed are:

- DB_PASSWORD:Password for the DB user name .
- DB_USER:User name of the DB which have the privilage to use the data.
- DB_NAME: Database name which is defined in Db container
- DB_HOST: The ip in which the DB container is hosted(since we made links, we need to give only the DB container name)
- SUPER_USERNAME=Username of API admin user
- SUPER_PASSWORD=password of API admin user
- SUPER_EMAIL=email of API admin user
- DEBUG_VAR= True / False (to set DEBUG variable in scrapy settings.py)

Since our container is in a network,we have to link them.Scraper container will be linked to DB container.Since this is a webservice, we have to open a port to access the api through web, ie, we are exposing port 80.

### Install Docker compose

``` pip install docker-compose ```
 Since we use multi containers, we are defining the docker compose file to make the container live in local.


### Insert url to Crawl
1.Create a csv file which contain the urls to crawl.File name as'urls.csv' 

2.Add this csv file to 'app-server' folder

### System Layout

![alt tag](https://raw.githubusercontent.com/sayonetech/automated-scraper/master/specs/SYSTEM-ARCHITECTUER.png)

### To build in LOCAL

1. Pull the repo to your local system.
2. Navigate to project folder. 
3. Update the path of Scraper Dockerfile in docker-compose.yml
4. To make the system run, use the following code 
   ```docker-compose up ```
    This command will automatically create the Docker image and will run the container .
5. To check whether the container is live or not, run the following code.
   ``` sudo docker ps ```
    This will show the live containers in system.There you can find our 3 containers.

The results will be shown in admin page, while running in local. Refer the api structure while it is running in live. 

