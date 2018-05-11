### Compiling ELL models

1. Build docker image
```
./build_docker.sh
```

2. Launch docker image
```
./launch_docker.sh
```

3. The import scripts can be found under the /scripts mapped volume in the docker instance.

4. Once import is done, copy the models while the docker instance is still running

Host:
```
# find the docker instance
docker ps

# copy models from the docker instance
cd ../pi/models
./copy_graphs.sh name_of_docker_instance
```