## Serverless sgcarmart monitoring

0. Obtain a Slack webhook url to post to a Slack channel:
https://api.slack.com/messaging/webhooks

1. Build container
```
sh build_docker.sh
```

2. Test container. Create an .env file with the SLACK_WEBHOOK_URL variable set. E.g.

.env:
```
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
```

Run using docker or udocker

```
# docker
sh launch_docker.sh

# udocker (see [](../README.md) for instructions on setting up virtual environment)
# this simulates running on AWS lambda
source py2/bin/activate
udocker run lisaong/monitor-carmart:1.0 --env-file=.env
```

3. Push container to docker registry
```
docker login
docker push lisaong/monitor-carmart:1.0
```

4. Create lambda and run it
```
scar init -f aws-lambda.yaml -e SLACK_WEBHOOK_URL=slack_webhook_url
scar run -f aws-lambda.yaml
```

![example.png](example.png)
