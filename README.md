# Bookstore micro services

## About this project

This repository is intended to store all the artifacts of the micro services needed to build a really simple bookstore software.

## Dependencies

Building the *commons* dependencies, responsible for storing the HTTP status codes:

*On the root folder*
```BASH
python setup.py sdist
```

Installing all dependencies:

*On the root folder*
```BASH
pip install -r requirements.txt
```

## How to run it

## How to contribute

```BASH
git clone https://github.com/williambrunos/Bookstore.git
git checkout -b <<your_branch_name>>
git add .
git commit -m "conventional commit message"
git push -u origin <<your_branch_name>>
```