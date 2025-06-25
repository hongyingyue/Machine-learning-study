# Docker
Docker is an open-source platform that simplifies the deployment of software applications by packaging them into containers. 

These containers act as lightweight, portable units that include everything needed to run the application across different environments.

## Why Use Containers?

Containers offer a streamlined way to isolate and deploy applications, ensuring they run consistently across various environments, whether on a developer’s laptop or the cloud. 

This isolation enhances portability and resource efficiency, making docker an essential tool for modern software development.

## Get your hands dirty

### Build docker image
```
docker build -t docker-demo:v1 .
docker build -t <image_name> <path_to_dockerfile>
# `-t` means tag
```

### Start a container
```
docker run docker-demo

# With Interactive Shell
docker run -it your-image-name /bin/bash
# or
docker run -it docker-demo:v1 sh

# To get out of the interactive shell, input `exit` in the shell.
```

| 🔧 Basic & Common Options                            | What It Does                                                               |
| --------------------------------- | -------------------------------------------------------------------------- |
| `-it`                             | Runs the container interactively with a TTY (good for shells)              |
| `--rm`                            | Automatically removes the container after it exits                         |
| `--name <name>`                   | Assigns a custom name to the container (easier than random names)          |
| `-d`                              | Detached mode — runs the container in the background                       |
| `-p <host_port>:<container_port>` | Maps a port on your machine to a port in the container (e.g. `-p 8000:80`) |
| `-v <host_path>:<container_path>` | Mounts a volume or folder into the container (for data persistence)        |

### Stop a container (if needed)
```
docker ps
docker stop <container_id_or_name>
```

### Remove containers
```
docker ps -a
docker rm <container_name_or_id> ...
```

### Remove images
```
docker image ls # List images by name and tag
docker rmi <image_name_or_id>
```


### Tag an image
Tag the image with the desired repository and name:
```
docker tag <image_name> <dockerhub_username>/<docker-repo-name>
```

### Push a Docker image
```
docker push <dockerhub_username>/<docker-repo-name>:latest
```