sudo docker rmi -f jwyeon/sherpa_data || true
sudo docker stop fastapi-container || true
sudo docker rm -f fastapi-container || true
sudo docker run -d -p 8000:8000 --name fastapi-container jwyeon/sherpa_data