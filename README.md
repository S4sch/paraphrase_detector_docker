# Paraphrase Detector (Docker)

A brief description of what this project does and who it's for.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Docker](https://www.docker.com/get-started).
- You have installed [Git](https://git-scm.com/downloads). You can verify the installation by running `git --version` in your command line.

## Cloning the Repository

To clone this repository, open up a command line and go to your working directory, in which you want the repository to be. Then you can clone it and go into the paraphrase directory.

```bash
cd yourdirectory/workingdirectory
git clone https://github.com/S4sch/paraphrase_detector_docker.git
cd paraphrase_detector_docker
```


Or you can just click on the green "Code" button and open it directly within Github Desktop, Visual Studio or directly download the ZIP.

![grafik](https://github.com/S4sch/paraphrase_detector_docker/assets/50823858/9cb0eba6-c722-4ce3-89b4-ecc7e65cc1a4)



If you have PyCharm, you can also use the git clone function there. For that you go to the "Git" Button, and from there to "Clone".

![grafik](https://github.com/S4sch/paraphrase_detector_docker/assets/50823858/c1ea244f-cba3-40ab-bcf2-82c8a9dcd1ce)


In the following window, you can then insert the link, https://github.com/S4sch/paraphrase_detector_docker.git and choose a directory and click on Clone. 

![grafik](https://github.com/S4sch/paraphrase_detector_docker/assets/50823858/9e652e84-ed41-4e2e-82c8-4c46ad000919)


## Building the Docker Image

To build the Docker image, run the following command. It is required to be in the same directory in which the Dockerfile of the repository is.

```bash
cd yourdirectory/workingdirectory/paraphrase_detector_docker
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

To stop the Docker container, use ```docker stop your-container-name```
To remove the Docker container, use ```docker rm your-container-name```
To remove the Docker image, use ```docker rmi your-image-name```





