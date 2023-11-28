# opp-api

## Team TMD: 
    - Trenton Creamer
    - Marcela Vijil 
    - Derek Laister

## Directions:
    - Add .env file 
        - Add a SECRET_KEY variable
        - Add an ALGORITHM variable


# Milestone 4A Submittal:
The docker file was built and used to generate a docker image. The docker image launched a docker container where
we were able to test our application. All of the rest API calls were working as expected in our testing. Below are all 
of the docker commands that we encountered when testing. 

Docker Image:
<br/>
<img src="./images/docker_image_1.png" alt="Docker Image" width="750">

Docker Log Info:
<br/>

<img src="./images/docker_container_log.png" alt="Docker Log" width="750">

Docker Container Running:
<br/>
<img src="./images/docker_container_running.png" alt="Docker Container" width="750">


## Docker-related commands

- docker build -t teamtmdimage:v1 . 
    - This is running the docker build command to generate our project image 
    - -t is letting us specify our name tag
    - . is looking at our root for a file called Dockerfile

- docker run --name teamtmdapp -p 8000:8000 teamtmdimage:v1
    - This command is launching our docker container from our image. 
    - --name is naming our container
    - -p is specifying our host(left) and apps(right) ports 
    - todoappimage:v1 this is telling which image and tag to run 

- docker stop teamtmdapp
    - stock our container by name 

- docker ps -a
    - look up all the contianers that we have 
    - ps stands for process status

- docker images
    - look up all of the docker images that we have 

- docker rmi ######
    - delete a docker image 

- docker rm #####
    - delete a docker container 

