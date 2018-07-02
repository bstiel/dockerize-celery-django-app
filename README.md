# How to Dockerize a Celery App With Django And RabbitMQ

This projects contains the source code examples accompanying the blog post:

https://www.python-celery.com/2018/06/05/celery-django-docker/.


Docker and docker-compose are highly recommended to run the example.

1. Bring up the docker stack:
```docker-compose up -d```

2. Rest API is available on http://localhost:8000

3. Show logs:
```docker-compose logs```

4. Monitor tasks in flower:
[http://localhost:5555](http://localhost:5555)

If you run without docker, make sure you run the services
specified in the docker-compose.yml file individually and
adjust the environment variables, ports etc as required.