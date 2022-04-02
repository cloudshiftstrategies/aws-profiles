# aws-profiles

A super simple tool to list all available named profiles in the ~/.aws/config file

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
Typically, this tool will be installed in your home directory
```
pip3 install --user --upgrade aws-profiles
```

## Contributing
#### Prerequisites
- python3.6+
- [poetry](https://python-poetry.org/docs/)

#### Installation and testing
```
poetry install
poetry run pytest --cov=src
poetry run black src
poetry run flake8 src
```

#### Committing
- commits must be formatted using angular commit format. Use `cz commit` to get help
- commits will be linted with a pre-commit-hook for commitizen

#### Publishing
- github actions uses symantec release to increment version and publish to pypi upon merge to main branch