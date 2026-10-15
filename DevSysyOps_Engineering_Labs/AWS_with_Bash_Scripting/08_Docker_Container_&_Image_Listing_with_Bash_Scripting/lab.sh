#!/bin/bash

echo "Listing Available Containers" 

containers=$(docker ps -a --format "{{.Names}}")

if [ -z "$containers" ]; then
  echo "No Containers Available Right Now"

else
  echo $containers	
  docker ps -a     	
	
fi  

echo "##################################################################################"
echo "##################################################################################"

echo "Listing Available Images"

images=$(docker images --format "{{.Repository}}")

if [ -z "$images" ]; then
  echo "No Available Images Right Now"

else
     docker images -a

fi     
