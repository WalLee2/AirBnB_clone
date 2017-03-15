#!/usr/bin/env bash
# Bash Script that sets up webservers for deployment.
sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "29i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
