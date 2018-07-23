from .celery import *
import environ
env = environ.Env()

broker_url = "amqp://"+env("RABBITMQ_USER")+":"+env("RABBITMQ_PASS")+"@"+env("RABBITMQ_HOST")+":5672/taiga"
result_backend = "redis://" + env("REDIS_HOST") + ":6379/0"
