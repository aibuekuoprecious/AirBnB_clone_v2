#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Update the package list and install Nginx
apt-get update
apt-get install -y nginx

# Create directory structure for web_static
WEB_ROOT="/data/web_static"
mkdir -p "$WEB_ROOT/releases/test"
mkdir -p "$WEB_ROOT/shared"
echo "Holberton School" > "$WEB_ROOT/releases/test/index.html"
ln -sf "$WEB_ROOT/releases/test/" "$WEB_ROOT/current"

# Set ownership and group for the web_static directory
chown -R ubuntu "$WEB_ROOT"
chgrp -R ubuntu "$WEB_ROOT"

# Configure Nginx server block
NGINX_CONFIG="/etc/nginx/sites-available/default"
printf "%s" "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias $WEB_ROOT/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > "$NGINX_CONFIG"

# Restart Nginx to apply the configuration changes
service nginx restart

