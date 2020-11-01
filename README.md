Meow facts
=====================

The service generates a random fact about cats.

The user connects to the websocket, Celery makes asynchronous requests to the api
, and when he receives a response, sends them over the websocket, every 5 sec in real-time

##### Tech stack:
* Websocket Django-channels
* Celery
* Redis as a message brocker
* Daphne as a ASGI application server
* Nginx
* Docker-compose

##### Link 
Сheck if my home server is running now:
* http://84.22.157.167:4444/meow/
