#!/bin/bash

# Default settings
IMAGE_NAME="foxy"
TAG="dev"
USER="dev"



echo "Using options:"
echo -e "\tImage name: $IMAGE_NAME"
echo -e "\tImage tag: $TAG"
echo -e "\tUser name: $USER"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo "Detected Linux "
  SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
  xhost +local:docker
  display=$DISPLAY
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
  echo "Detected Windows"
  SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd -W)
  display=host.docker.internal:0.0
  display=$DISPLAY
fi
echo "Launching image!"


# -v ~/.gitconfig:/etc/gitconfig
#   --gpus all \
docker run -it --rm --privileged --name EB23 \
    -v $SCRIPT_DIR/workspace:/home/$USER/workspace \
    -v $SCRIPT_DIR/resources:/home/$USER/resources \
    -v build:/home/$USER/workspace/build/ \
    -v log:/home/$USER/workspace/log/ \
    -v install:/home/$USER/workspace/install/ \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix \
    -p 9090:9090 -p 8050:8050 \
    --env DISPLAY=$display \
    $IMAGE_NAME:$TAG