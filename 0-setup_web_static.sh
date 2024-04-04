#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/



echo "Holberton School" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static
echo "server {
    listen 80;
    server_name _;
         root /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
    }
    location / {
        # Your other configuration directives, if any
    }
}" > /etc/nginx/sites-available/default

# sudo nginx -t
sudo service nginx restart
