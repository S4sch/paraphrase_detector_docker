# Paraphrase Detector with Docker

This repository contains a Docker setup for training a paraphrase detection model. The model configuration has been optimized by myself and is ready to achieve a good performance within a maximum of three training epochs. The training process is automated and starts as soon as the Docker container is built and runs.

## Prerequisites

Before proceeding, ensure the following requirements are met:

- Docker Desktop is installed on your system. Launch Docker Desktop to ensure it is running before building your Docker image. You can download it from [Docker](https://www.docker.com/get-started).
- If you prefer using the command line for Git operations, make sure you have [Git](https://git-scm.com/downloads) installed. Verify the installation by executing `git --version` in your terminal.

## Cloning the Repository

To clone this repository, execute the following commands in your terminal, making sure you're in the directory where you want the repository:


```bash
cd path/to/your/working/directory
git clone https://github.com/S4sch/paraphrase_detector_docker.git
cd paraphrase_detector_docker
```


Alternatively, you can download the repository directly from the GitHub interface. Click the green "Code" button on the repository page and select "Download ZIP," or use the GitHub Desktop or Visual Studio options to clone the repository.

![grafik](https://github.com/S4sch/paraphrase_detector_docker/assets/50823858/9cb0eba6-c722-4ce3-89b4-ecc7e65cc1a4)



For PyCharm users, utilize the IDE's Git integration, for that you go to the "Git" Button, and from there to "Clone".

![grafik](https://github.com/S4sch/paraphrase_detector_docker/assets/50823858/c1ea244f-cba3-40ab-bcf2-82c8a9dcd1ce)


In the following window, you can then insert the link, https://github.com/S4sch/paraphrase_detector_docker.git and choose a directory and click on Clone. 

![grafik](https://github.com/S4sch/paraphrase_detector_docker/assets/50823858/9e652e84-ed41-4e2e-82c8-4c46ad000919)


## Building the Docker Image

To build the Docker image, run the following command. It is required to be in the same directory in which the Dockerfile of the repository is. Make sure that the Docker Desktop application is running, as discussed in the Prerequisites.

```bash
cd path/to/your/working/directory/paraphrase_detector_docker
docker build -t paraphrase-detection .
```
Replace paraphrase-detection with the name you wish to give the Docker image.


## Running the Docker Container

After building the image, you can run the Docker container with:

```bash
docker run --name paraphrase-detection-container paraphrase-detection
```

Replace paraphrase-detection-container with the name you want to assign to your container.
You can add a -d flag inside of the docker run command, if you want the container to be in the background and continue using the terminal session.


### Additional Information

To stop the Docker container, use ```docker stop your-container-name```.
To remove the Docker container, use ```docker rm your-container-name```.
To remove the Docker image, use ```docker rmi your-image-name```.









