
#!/bin/bash

echo "Available Docker Containers"

echo "------#######################------"

docker ps -a 

read -p "Enetr the Container name to run" container_name

if docker ps -a --format "{{.Names}}" | grep -qx "$container_name"; then 
	echo "Conatiner Available: $container_name"
	echo "Starting Container"
        docker start "$container_name"

else
        echo "Container not found"
        echo "Pulling Container"
        docker pull "$container_name"

        echo "Creating & Starting Container.........."
        docker run -d --name "$container_name" "$container_name"

fi	
        






