#!/bin/bash

#cd /home/pi
#git clone https://github.com/fastcarsub88/rain_gauge.git
#cd rain_gauge
sudo rm /etc/nginx/sites-enabled/nginx_conf
sudo ln -s /home/pi/rain_gauge/nginx_conf /etc/nginx/sites-enabled/
sudo nginx -s reload
sudo systemctl link /home/pi/rain_gauge/rain_gauge.service
sudo systemctl link /home/pi/rain_gauge/rain_gauge_api.service
sudo systemctl enable rain_gauge
sudo systemctl enable rain_gauge_api
