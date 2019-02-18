#!/bin/bash

echo "Initializtaion started"

#pip
pip install Kqlmagic --no-cache-dir --upgrade
pip install -r msticpy/requirements.txt
pip install --upgrade dnspython
pip install --upgrade ipwhois
pip install --upgrade folium
pip install --upgrade maxminddb-geolite2
pip install --upgrade pandas