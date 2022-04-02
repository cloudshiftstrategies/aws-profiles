# aws-profiles

A super simple tool to list all available named profile in the ~/.aws/config file

This is useful when you have a lot of profiles defined and can never remember the exact
names to use in an aws cli command like `aws s3 list --profile XXXX` or when setting the
env variable `AWS_PROFILE`

## Usage

Assuming you had three profiles named profile1, profile2 & profile3 defined in your ~/.aws/config file
```
$ aws_profiles list

profile1
profile2
profile3
```

## Requirements
* python3.6+

## Installation
```
pip3 install aws-profiles
```

## Contributing

#### Testing
```
poetry run pytest --cov
```