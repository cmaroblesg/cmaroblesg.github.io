---
layout: post
toc: true
title: "Building a Python Development Docker Container for AI and Data Science"
categories: [Containers]
tags: [Docker]
author: César Robles
---
Creating a robust development environment is crucial for AI and data science projects. Here’s how you can build a Docker container with Python 3.12, essential libraries, Jupyter Lab, and Visual Studio Code.

## Dockerfile

Here’s the Dockerfile to set up the container:
[Dockerfile](/documents/Dockerfiles/Dockerfile_Python3.12_JupyterLab_VSCode)

```dockerfile
# Use an Ubuntu base image
FROM ubuntu:20.04

# Update packages and install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    wget \
    curl \
    git \
    build-essential

# Add the Python 3.12 PPA and install Python 3.12
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3.12-dev python3-pip

# Create a symbolic link so python points to python3.12
RUN ln -s /usr/bin/python3.12 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# Install required Python libraries
RUN pip install --upgrade pip && \
    pip install openai streamlit pandas numpy openpyxl jupyterlab

# Install Visual Studio Code Server
RUN wget -qO- https://aka.ms/install-vscode-server/setup.sh | bash

# Expose ports
EXPOSE 8888
EXPOSE 8080

# Create a non-root user to work with
RUN useradd -ms /bin/bash devuser

# Switch to the created user
USER devuser
WORKDIR /home/devuser

# Command to start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

## Step-by-Step Guide to Building the Container
### 1. Create the Dockerfile:
* Open a terminal and create a new directory for your project:
```bash
mkdir python_dev_container
cd python_dev_container
```
* Create a file named Dockerfile:
```bash
nano Dockerfile
```
* Copy and paste the Dockerfile content provided above into the Dockerfile and save the changes.

### 2. Build the Docker Image:
* Ensure you have Docker installed on your system. If not, you can install it following the instructions [here](https://www.docker.com/products/docker-desktop).
* In the directory where you created the Dockerfile, run the following command to build the image:
```bash
docker build -t python_dev:latest .
```

### 3. Run the Container:
* Once the image is built, run the container using:
```bash
docker run -it -p 8888:8888 -p 8080:8080 python_dev:latest
```
* This will start the container and expose ports 8888 for Jupyter Lab and 8080 for Visual Studio Code.

### 4. Access Jupyter Lab and Visual Studio Code:
Open your browser and go to [http://localhost:8888](http://localhost:8888) to access Jupyter Lab.
For Visual Studio Code, open your browser and go to [http://localhost:8080](http://localhost:8080).
This container provides a complete development environment with Python 3.12, necessary libraries, Jupyter Lab, and Visual Studio Code, all ready to use.