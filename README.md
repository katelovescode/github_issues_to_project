# Add Github Issues to Project (Beta)

A python script to move Github issues to a next-gen (beta) Github Project 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before installing the software.

* Python
* A Github personal access token
* A Github next-gen (beta) project
* A Github repository with issues in it

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ pip install -r requirements.txt
$ export GITHUB_TOKEN=[github personall access token] # this is optional, if this env var isn't set the script will ask for it
```

## Usage

A few examples of useful commands and/or tasks.

Basic usage:

```
$ python3 github_issues_to_project -o [organization name] -r [repository name] -p [project number from URL bar]
```

The script will list the first 30 issues from that repo and ask for confirmation that you want to add them to the project.  If you confirm with `Y`/`y` it will add those issues to the project.  If you type anything else it will exit.

## Contributing

See the [contributing guidelines](CONTRIBUTING.md) for more info about contributing to this repository.

## Code of Conduct

This repository is governed by a [Code of Conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with this project.