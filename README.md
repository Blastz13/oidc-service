
# Installation and launch

**Installation**

You can clone this application:

```bash 
git clone https://github.com/Blastz13/city_events
```

You need to define environment variables in the **.env** file to run the application in docker.
An example file with environment variables is located in the **.env.example** file.

Next, you need to run the project using docker from the root directory:

```bash
docker-compose -f ./docker/docker-compose.yml up -d --build
```

# Manual Launch

You can clone this application:

```bash 
git clone https://github.com/Blastz13/oidc-service
```

You need to define environment variables in the **.env** file to run the application.
An example file with environment variables is located in the **.env.example** file.

Next, you need to install the necessary libraries:

### Poetry

```bash
poetry install
poetry update
poetry shell
```

### Pip

```bash
pip3 install -r requirements.txt
```

## Generating and applying database migrations

```bash
alembic revision --autogenerate -m '<comment>'
alembic upgrade head
```

Now you can start the server:

```bash
uvicorn app.server:app --host 0.0.0.0 --port 8000 --reload
```

OR

```bash
python3 main.py --env test|local|dev|prod --debug
```

## Launching celery

Celery Worker

```bash
 celery -A celery_app.celery_app worker --loglevel=info
```

Celery Beat

```bash
celery -A celery_app.celery_app beat --loglevel=info
```

## Swagger

Swagger is located at the following address: http://0.0.0.0:8000/docs

## Running tests

```bash
pytest -s -p no:warnings --cov
```


### License

Copyright © 2023 [Blastz13](https://github.com/Blastz13/).