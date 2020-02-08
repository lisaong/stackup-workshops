## Serverless sgcarmart monitoring

1. Obtain a Slack webhook url to post to a Slack channel:
https://api.slack.com/messaging/webhooks

2. Build container
  ```
  sh build_docker.sh
  ```

3. Test container with shell environment variables, then run either docker or udocker: 

  ```
  cat >> .env << EOF
  SLACK_WEBHOOK_URL=https://hooks.slack.com/xxx
  CARMART_QUERIES=mx-5;brz;toyota+86
  EOF

  # docker
  sh launch_docker.sh

  # udocker (see [](../README.md) for instructions on setting up virtual environment)
  # this simulates running on AWS lambda
  source py2/bin/activate
  udocker run lisaong/monitor-carmart:1.0 --env-file=.env
  ```

4. Push container to docker registry
  ```
  docker login
  docker push lisaong/monitor-carmart:1.0
  ```

5. Create lambda and run it
  ```
  scar init -f aws-lambda.yaml -e SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL
  scar run -f aws-lambda.yaml
  ```

![example.png](example.png)

6. Schedule the lambda to run periodically. For example, using cron expressions: cron(0 9,21 * * ? *)

https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html

![example2.png](example2.png)
