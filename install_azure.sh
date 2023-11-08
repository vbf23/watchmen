#!/bin/bash

# Update the system
sudo apt update

# Install Python3 and pip3
sudo apt install python3 -y
sudo apt install python3-pip -y

# Install Flask
pip3 install Flask

# Install HTTP Server (Apache)
sudo apt install apache2 -y

# Start and enable Apache
sudo systemctl start apache2
sudo systemctl enable apache2

# Allow HTTP traffic in the firewall
sudo ufw allow 'Apache'
sudo ufw --force enable
