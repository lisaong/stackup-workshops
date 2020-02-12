## Serverless sgcarmart monitoring

This example demonstrate running a AWS Lambda periodically (every few hours) to monitor SGCarMart listings:
* Scrape listing information using BeautifulSoup
* Post to a Slack channel using a Webhook
* Persist the most recently scraped listing information, and used this to flag new listings for the user 

### Setup

1. Obtain a Slack webhook url to post to a Slack channel:
https://api.slack.com/messaging/webhooks

2. Create an S3 bucket, e.g. 'carmart'. Configure a policy similar to this for your lambda's IAM user so that it can read/write objects to the folder. This bucket can be private.
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

4. Test container with pre-configured shell environment variables. To setup AWS credentials, see [the top level README](../README.md).

```
cat >> .env << EOF
SLACK_WEBHOOK_URL=https://hooks.slack.com/xxx
CARMART_QUERIES=mx-5;brz;toyota+86
S3_BUCKET_NAME=carmart
AWS_SHARED_CREDENTIALS_FILE=/aws/credentials
AWS_CONFIG_FILE=/aws/config
EOF

# run docker, mapping ~/.aws to /aws
sh launch_docker.sh
```

5. Push container to docker registry.
```
docker login
docker push lisaong/monitor-carmart:1.0
```

6. [Optional] Test with udocker to simulate Lambda environment. See [the top level README](../README.md) for instructions on setting up udocker. udocker requires the container to be already in the docker registry.
```
source py2/bin/activate
udocker run --env-file=.env --volume=$HOME/.aws:/aws lisaong/monitor-carmart:1.0
```
Refer to https://github.com/indigo-dc/udocker/blob/master/doc/user_manual.md for more commands. If updating the container, you may want to run `udocker rmi -f lisaong/monitor-carmart:1.0` so that udocker will pull the latest version.

7. Create lambda and run it. Make sure date is set correctly in the system `sudo date +%T%p -s "6:13PM"` if running on VirtualBox VM.
```
# set variables that are not specified in the yaml
export SLACK_WEBHOOK_URL=...
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...

scar init -f aws-lambda.yaml -e SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

scar run -f aws-lambda.yaml
```

![example.png](example.png)

8. Schedule the lambda to run periodically. For example, using cron expressions: cron(0 9,21 * * ? *)

https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html

![example2.png](example2.png)
