sudo docker rmi -f jwyeon/sherpa_fe || true
sudo docker stop react-container || true
sudo docker rm -f react-container || true
sudo docker run -d -p 3000:3000 --name react-container --env-file /home/scripts/.env jwyeon/sherpa_fe
