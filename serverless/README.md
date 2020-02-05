# Serverless Examples

## Setup
1. Install AWS CLI and use it to configure AWS credentials
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
```
aws2 configure
```

More info on AWS Access Keys: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

2. Install SCAR, which requires AWS credentials
https://scar.readthedocs.io/en/latest/installation.html

Once installed, SCAR can be used to run Docker containers within AWS Lambdas

## Examples:
- [monitor sgcarmart listings](carmart)

## References:
- https://medium.com/@michalyanko/how-many-ways-are-there-to-schedule-a-task-bd1cc7b57f28