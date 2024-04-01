# First Dockerfile for a Python API Application
# The Dockerfile will give instructions of how to build a machine from scratch

# Set the base image to use the subsequent instructions, this will make a O.S with ubunto and Python inside thid "Docker Machine"
FROM python:3

# Convention: this line below will make the working directory to be at user/source/app, we usually put our user work directory at this path.
WORKDIR /usr/src/app

# Those 2 lines below are coping and installing the requirements to our application works correctly, so basically will install flask at this application.
COPY requirements.txt .
# This line, with those flags, ensures that the latest versions of packages are always installed and installs all the packages listed in the requirements file along with their dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copying the current files at web directory into our built machine
COPY . .

# Running Pyhton and app.py
CMD ["python", "API.py"]