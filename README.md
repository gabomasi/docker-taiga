Deploy your Taiga services with Docker
========================================

> Taiga is a project management platform for agile developers & designers
> and project managers who want a beautiful tool that makes work truly
> enjoyable.
>
> https://taiga.io/

Goodies
-------

* Python 3.6
* Postgres 10
* Alpine Linux images
* Gevent worker for gunicorn
* django-anymail integration
* Gitlab integration
* Mailgun configuration

I've tried to containerize every module, so we have:

* frontend
* backend
* celery worker
* redis
* rabbitmq
* events

Quickstart
----------

I'm going to write some better instructions soon, but for now, if you want to
try it, just type:

```
docker-compose up
```

PS: since the frontend port is mapped to 80, just go to your browser and http://localhost. The login credentials are **admin** with password **123123**.


Credits
-------

* https://taigaio.github.io/taiga-doc/dist/setup-production.html
* https://github.com/taigaio/taiga-contrib-gitlab-auth
* https://github.com/douglasmiranda/docker-taiga
* https://github.com/ipedrazas/taiga-docker

Inspired by:

* https://github.com/benhutchins/docker-taiga
* https://github.com/ipedrazas/taiga-docker
