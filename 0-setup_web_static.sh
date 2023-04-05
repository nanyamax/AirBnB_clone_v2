#!/usr/bin/env bash

# Install Nginx if not already installed
apt-get update
apt-get -y install nginx

# Create necessary directories and files for web_static
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo '<html><head></head><body>Holberton School</body></html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

# Update Nginx config to serve web_static files
sed -i '51 i \\\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
service nginx restart
