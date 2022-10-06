# python-flask-pymongo-docker

[![Language](https://img.shields.io/badge/language-python3-brightgreen)](https://www.python.org/)

Basic RESTful API with Python and MongoDB using Flask microframework with PyMongo. The project uses Docker (docker-compose).

## Stack

- Python 3
- Flask
- Flask-RESTPlus
- PyMongo
- Docker

## Usage

[Install Docker](https://www.docker.com/products/docker-desktop) if you don't have it yet and run the container:

```sh
$ docker-compose up
```

It will run both Web and Mongodb containers in Development environment on `localhost:5000`.

## Structure


```
├── app.py - Entry point of application
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt - Dependencies
```