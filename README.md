# How to Dockerize a Celery App With Django And RabbitMQ

This projects contains the source code examples accompanying the blog post:

https://www.python-celery.com/2018/06/05/celery-django-docker/.


Docker and docker-compose are highly recommended to run the example.

1. Bring up the docker stack:
```docker-compose up -d```

2. Rest API is available on http://localhost:8000

3. Trigger timeseries request:
```curl -d '{"database_code":"WIKI", "dataset_code":"FB"}' -H "Content-Type: application/json" -X POST http://localhost:8000```

4. Check logs:
```docker-compose logs -f```

5. List cached timeseries:
```curl -X GET http://localhost:8000```

6. Get timeseries:
```curl -X GET http://localhost:8000/WIKI-FB```

6. Monitor tasks in flower:
[http://localhost:5555](http://localhost:5555)

If you run without docker, make sure you run the services
specified in the docker-compose.yml file individually and
adjust the environment variables, ports etc as required.