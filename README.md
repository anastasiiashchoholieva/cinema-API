# Cinema API

***

API service for cinema management written on DRF
## Installing using GitHub

***
Install PostgresSQL and create db

create .env by example:
```python
POSTGRES_HOST=<your db hostname>
POSTGRES_DB=<your db name>
POSTGRES_USER=<your db username>
POSTGRES_PASSWORD=<your db password>
```


```python
git clone https://github.com/anastasiiashchoholieva/cinema-API.git
cd cinema_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## Run with docker
***
https://hub.docker.com/r/anastasiia1601/cinema-api

Docker should be installed

```python
docker-compose build
docker-compose up
```

## Getting access
***
- create user via /api/user/register/
- get access token via /api/user/token/

## Features
***
- JWT authenticated
- Admin panel /admin/
- Documentation is located at /api/doc/swagger/
- Managing orders and tickets
- Creating movies with genres, actors
- Creating cinema halls
- Adding movie session
- Filtering movies and movie session
