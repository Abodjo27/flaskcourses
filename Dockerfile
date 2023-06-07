FROM python:3

# Installation de python3-pip
RUN apt-get update && apt-get install -y python3-pip

# Mise à jour de pip
RUN pip3 install --upgrade pip
