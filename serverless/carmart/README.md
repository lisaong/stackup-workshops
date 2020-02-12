## Serverless sgcarmart monitoring

1. Obtain a Slack webhook url to post to a Slack channel:
https://api.slack.com/messaging/webhooks

2. Create an S3 bucket, e.g. 'carmart'. Configure a policy similar to this for your lambda's IAM user so that it can read/write objects to the folder:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "xxxxx",
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:ListObjects",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::carmart"
            ]
        }
    ]
}
```

3. Build container
  ```
  sh build_docker.sh
  ```

4. Test container with shell environment variables, then run either docker or udocker: 

  ```
  cat >> .env << EOF
  SLACK_WEBHOOK_URL=https://hooks.slack.com/xxx
  CARMART_QUERIES=mx-5;brz;toyota+86
  S3_BUCKET_NAME=carmart
  EOF

  # docker
  sh launch_docker.sh

  # udocker (see ../README.md) for instructions on setting up virtual environment)
  # this simulates running on AWS lambda
  source py2/bin/activate
  udocker run --env-file=.env lisaong/monitor-carmart:1.0
  ```

5. Push container to docker registry
  ```
  docker login
  docker push lisaong/monitor-carmart:1.0
  ```

6. Create lambda and run it. Make sure date is set correctly in the system `sudo date +%T%p -s "6:13PM"` if running on VirtualBox VM.
  ```
  scar init -f aws-lambda.yaml -e SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL
  scar run -f aws-lambda.yaml
  ```

![example.png](example.png)

7. Schedule the lambda to run periodically. For example, using cron expressions: cron(0 9,21 * * ? *)

https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html

![example2.png](example2.png)
