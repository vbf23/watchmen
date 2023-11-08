#!/bin/bash

# Update the system
sudo yum update -y

# Install Python3 and pip3
sudo yum install python3 -y
sudo alternatives --set python /usr/bin/python3
sudo yum install python3-pip -y

# Install Flask
pip3 install Flask

# Install HTTP Server (Apache)
sudo yum install httpd -y

sudo yum install git -y

# Start and enable Apache
sudo systemctl start httpd
sudo systemctl enable httpd

# Allow HTTP traffic in the firewall
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
