#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Update package index and install Nginx if not already installed
sudo apt update
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a test HTML file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static
if ! grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
    sudo sed -i '/server_name _;/a \    location /hbnb_static {\n        alias /data/web_static/current;\n    }' /etc/nginx/sites-available/default
fi

# Restart Nginx
sudo service nginx restart

