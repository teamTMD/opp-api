# opp-api
Project opp-api

## Directions:
    - Add .env file 


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

