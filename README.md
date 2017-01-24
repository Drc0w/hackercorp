# HackerCorp

Hello World!

We are the HackerCorp team. The name has nothing to do with our activities, we
just enjoy to write articles on
things we enjoy. This is mainly around programming or playing with some boards.
Recently, we decided to open-source
our articles on GitHub, but you can check the result on
[our blog](https://www.hackercorp.eu).

## Setup

Our blog is generated with `pelican`, if you want to try it locally, you will
need to run the following steps:
```
git clone --recursive https://github.com/Drc0w/hackercorp.git
```
If you are using `virtualenv`, you should run:
```
virtualenv venv --python=/usr/bin/python3
source venv/bin/activate
```
In order to install the packages needed to run `pelican`, you will have to run:
```
pip install -r requirements.txt
```

## Build

In order to build the static website from the Markdown files, you will have to
run:
```
make html patch serve
```
Thanks to the rule `serve`, you can access the result locally on
`localhost:8000`. You can refer to `Pelican` documentation for 
more informations.
