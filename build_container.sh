#!/bin/bash

# Default settings
IMAGE_NAME="foxy"
TAG="dev"
USER_NAME="dev"

function usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "    -i,--image-name                    Set docker image name."
    echo "                                       Default: $IMAGE_NAME"
    echo "    -t,--tag                           Set tag of the image"
    echo "                                       Default: $TAG"
    echo "    -u,--user-name                     Set user name."
    echo "                                       Default: $USER_NAME"
    echo "    -h,--help                          Display the usage and exit."
}

OPTS=`getopt --options i:hi:n:t:u: \
         --long image-name:,help,tag:,user-name: \
         --name "$0" -- "$@"`
eval set -- "$OPTS"

while true; do
  case $1 in
    -h|--help)
      usage
      exit 0
      ;;
    -i|--image-name)
      IMAGE_NAME="$2"
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
    --)
      if [ ! -z $2 ];
      then
        echo "Invalid parameter: $2"
        exit 1
      fi
      break
      ;;
    *)
      echo "Invalid option"
      exit 1
      ;;
  esac
done

echo "Using options:"
echo -e "\tImage name: $IMAGE_NAME"
echo -e "\tuser name: $USER_NAME"
echo -e "\ttag:  $TAG"
echo "Building image!"
docker volume rm build install log
docker build -t $IMAGE_NAME:$TAG --build-arg user=$USER_NAME --build-arg uid=$(id -u) --build-arg gid=$(id -g) .
