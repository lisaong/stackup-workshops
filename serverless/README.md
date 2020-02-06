# Serverless Examples

## Setup
1. Install AWS CLI and use it to configure AWS credentials
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
```
aws configure
```

More info on AWS Access Keys: 
https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys

From AWS Console, create an Inline Policy for the IAM Role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:*"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::*"
    }
  ]
}
```

Once the role is created, get the Role ARN (arn:aws:iam:...). This will be used to update `$HOME/.scar/scar.cfg` in the next step.

2. Install SCAR, which requires AWS credentials
https://scar.readthedocs.io/en/latest/installation.html

If using pip3 install, add the following to .bashrc after installation:
```
export PATH=$PATH:$HOME/.local/bin
```

Update `$HOME/.scar/scar.cfg` to specify the IAM Role:

```
{
  "scar": {
    "config_version": "1.0.9"
  },
  "aws": {
    "iam": {
      "boto_profile": "default",
      "role": ""  <-- update this
    },

  ...
}
```



Once installed, SCAR can be used to run Docker containers within AWS Lambdas

## Examples:
- [monitor sgcarmart listings](carmart)

## References:
- https://medium.com/@michalyanko/how-many-ways-are-there-to-schedule-a-task-bd1cc7b57f28
