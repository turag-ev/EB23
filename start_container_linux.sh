#!/bin/bash

# Default settings
IMAGE_NAME="foxy"
TAG="dev"
NETWORK="host"
USER="dev"

function usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "    -i,--image-name                    Set docker image name."
    echo "                                       Default: $IMAGE_NAME"
    echo "    -n,--network                       Set name of virtual docker network"
    echo "                                       Default: $NETWORK"
    echo "    -t,--tag                           Set tag of image."
    echo "                                       Default: $TAG"
    echo "    -u,--user-name                     Set docker user name."
    echo "                                       Default: $USER_NAME"
    echo "    -h,--help                          Display the usage and exit."
}

while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
      usage
      exit 0
      ;;
    -i|--image-name)
      IMAGE_NAME="$2"
      shift 2
      ;;
    -n|--network)
      NETWORK="$2"
      shift 2
      ;;
    -t|--tag)
      TAG="$2"
      shift 2
      ;;
    -u|--user-name)
      USER_NAME="$2"
      shift 2
      ;;
    -*|--*)
      echo "Invalid argument: $1 or parameter: $2"
      exit 1
      ;;
    *)
      echo "Invalid option"
      exit 1
      ;;
  esac
done

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Using options:"
echo -e "\tImage name: $IMAGE_NAME"
echo -e "\tImage tag: $TAG"
echo -e "\tUser name: $USER"
echo -e "\tvirtual network (currently not used): $NETWORK"
echo "Launching image!"
xhost +local:docker
# -v ~/.gitconfig:/etc/gitconfig
# sudo chgrp video /dev/dri/renderD128 && \
docker run -it --rm --privileged \
    -v $SCRIPT_DIR/workspace/python_packages:/home/$USER/workspace/python_packages \
    -v $SCRIPT_DIR/workspace/ros_packages:/home/$USER/workspace/ros_packages \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix \
    --net=$NETWORK \
    --env DISPLAY=$DISPLAY \
    $IMAGE_NAME:$TAG