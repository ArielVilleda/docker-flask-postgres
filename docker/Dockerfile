FROM python:3.9.1-slim-buster

# Initialize and Prepare
WORKDIR /data/web

# Copying the requirements.txt file first
COPY /project/requirements.txt /data/web/
# Install python requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# In the last steps of Dockerfile, coopying the others files 
# to avoid reinstallation of dependecies if files changes
COPY /project /data/web/
