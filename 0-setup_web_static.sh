#!/usr/bin/env bash
# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories and files for web_static
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo '<html><head></head><body>Holberton School</body></html>' > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
# Update Nginx config to serve web_static files
sudo sed -i '51 i \\\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
service nginx restart
