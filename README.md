# Zijing's Project2
Command line bash tool.

## Key Objectives of Project
In project 2, I build up a Bash command-line tool that performs data analysis task. And build docker container to deploy and run it.

## Structure Diagram
![phrase-repeater-docker](https://user-images.githubusercontent.com/58792/191573025-72d39f65-4dbb-4cd5-b4a3-80f6f45ff05e.png)

## Demo Video Link
https://github.com/nogibjj/Zijing-proj2/blob/main/demo-video.mp4

##  Main Steps
### 1. Build python command line file 
* In query.py, build up 2 command describe and query-most-n
* In app.py, build up streamlit app to build up web front, display and do word count analysis.

### 2. Create a new bash file
`sh command.sh` to run query.py and app.py

### 3. Docker build process
* install docker 
* build `docker build .`
* list `docker image ls`
* run with image id `docker run -it 93e112b1a2e7 /bin/bash command.sh`

### Push to DockerHub
* docker login: `docker login -u <hub-user -p $DOCKER_HUB`
* build and tag locally: `docker build . -t <hub-user>/<repo-name>`
* docker push 
`docker push wanzijin/proj2`

### Push in Cloud9

* create Cloud9 environment and ECR repository
* connect ECR 
`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 216514549505.dkr.ecr.us-east-1.amazonaws.com`
* retag 
`docker tag wanzijin/proj2 216514549505.dkr.ecr.us-east-1.amazonaws.com`
* push to ECR
`docker push 216514549505.dkr.ecr.us-east-1.amazonaws.com/proj2:latest`
* run docker
`docker run -it 216514549505.dkr.ecr.us-east-1.amazonaws.com/proj2:lastest /bin/bash command.sh`
