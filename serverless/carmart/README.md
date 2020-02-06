## Serverless sgcarmart monitoring

1. Build container
```
sh build_docker.sh
```

2. Test container

```
# docker
sh launch_docker.sh

# udocker (see [](../README.md) for instructions on setting up virtual environment)
# this simulates running on AWS lambda
source py2/bin/activate
udocker run lisaong/monitor-carmart:1.0
```

3. Push container to docker registry
```
docker login
docker push lisaong/monitor-carmart:1.0
```

4. Create lambda and run it
```
scar init -f aws-lambda.yaml
scar run -f aws-lambda.yaml
```

![example.png](example.png)