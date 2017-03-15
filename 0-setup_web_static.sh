#!/usr/bin/env bash
# Bash Script that sets up webservers for deployment.
sudo apt-get install -y nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
"$touch /data/web_static/releases/test/index.html"
"$ln -fs /data/web_static/current" "/data/web_static/releases/test/"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "29i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
