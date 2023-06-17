# scanner-service

To use this Makefile, follow these steps:

    Open a terminal and navigate to the directory where the Makefile is located.

    Run make build to build the Docker image. This command will build the image and tag it with the name my_fastapi_app. 
    You can change the tag in the Makefile if desired.

    Once the image is built, run make run to start a container from the image. This command will bind port 8000 on your host machine to port 8000 in the container.

    Access your FastAPI app by visiting http://localhost:8000. The app will be running inside the Docker container.

    To stop the running container, run make stop. This command will stop the container associated with the my_fastapi_app image.

    If you want to remove all unused Docker resources (containers, images, networks, and volumes), run make clean. Use this command with caution, as it will delete all unused Docker resources.