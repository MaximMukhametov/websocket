import logging

import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
logger = logging.getLogger()


@shared_task
def get_random_fact():
    # request to a third-party api, and getting random fact about cats
    res = requests.get("https://meowfacts.herokuapp.com/").json()
    fact = res["data"][0]

    # logging to see that the worker has started
    logger.info(fact)

    # sending a message
    async_to_sync(channel_layer.group_send)(
        "meow_facts", {"type": "meow_facts.fact", "text": fact}
    )
