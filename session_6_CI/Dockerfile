# This is the base-image for the Dockerfile
FROM python:3.10-slim 
# This is debian-based image with Python 3.10

# Set the working directory in the container
WORKDIR /flask-loan-app


COPY artefacts/requirements.txt /flask-loan-app/requirements.txt
# This copies the requirements.txt file from the host to the container

# Install the dependencies
RUN pip install -r /flask-loan-app/requirements.txt
# RUN executes only once when the image is built

COPY . /flask-loan-app/

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]

# python -m flask -app hello.py run --host=0.0.0 --port=8000

# CMD runs the command when the container starts



#docker build -t mark1 .
#docker image ls
#docker run -p 8000:8000 mark1
#docker run -p 8000:8000 --name flask-loan-app-container mark1


#docker run -d -p 8000:8000 mark1
# -d flag is for detached mode, which runs the container in the background

#docker container run -it -p 8000:8000 mark2 bash
# -it flag is for interactive mode, which allows you to interact with the container's shell

# first 8000 is the port on the host machine (my local) and the second 8000 is the port on the container

#docker container ls --all

# this will tell us the container id, which we can use to stop the container

#swarms

#docker image tag mark2:latest shivam13juna/example2-docker:latest

#https://hub.docker.com/r/shivam13juna/june11-mlops