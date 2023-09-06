#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
#sudo apt-get update
#sudo apt-get install -y nginx
sudo mkdir /data
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/releases/test/
sudo echo "Hello worl" | sudo tee /data/web_static/releases/test/index.html
sudo rm  -r /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
new_location="server {\n\t
        listen 80 default_server;\n\t
        listen [::]:80 default_server;\n\t
        root /var/www/html;\n\t
        index index.html index.htm index.nginx-debian.html;\n\t
        server_name _;\n\t
        location /404.html {\n\t\t
                add_header X-Served-By $HOSTNAME;\n\t
        }\n\t
        location / {\n\t
                # First attempt to serve request as file, then\n\t\t
                # as directory, then fall back to displaying a 404.\n\t\t
                try_files $uri $uri/ =404;
                add_header X-Served-By $HOSTNAME;\n\t
        }\n
        location /redirect_me {\n\t\t
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t
                add_header X-Served-By $HOSTNAME;
        }\n
	location /hbnb_static {
		alias /data/web_static/current/;
	}
        error_page 404 /404.html;\n\t
        add_header X-Served-By $HOSTNAME;\n
}"
echo -e "$new_location" | sudo tee /etc/nginx/sites-enabled/default > /dev/null 2>&1
sudo service nginx restart
