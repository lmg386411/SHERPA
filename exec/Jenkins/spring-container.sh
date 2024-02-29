#!/bin/sh

sudo docker rmi -f jwyeon/sherpa_be || true
sudo docker stop spring-container || true
sudo docker rm -f spring-container || true
sudo docker run -d -p 8080:8080 --name spring-container --env-file /home/scripts/.env jwyeon/sherpa_be