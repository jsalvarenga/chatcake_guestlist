from confluent_kafka import Consumer, Producer

from chatcake_client import AppRunner
from guestlist.guestlist import GuestList

import os

os.environ()


config = {
    'servers': 'pkc-43n10.us-central1.gcp.confluent.cloud:9092',
    'username': 'CGHXESKYEY2GQFZQ',
    'password': 'Ko5GtdXSPuLGz81jVOQk6bLar6fOWPTPfLVtuw2gcFstFbeHIboJHwhEwUFbOvpN',
    'id': 'teste'
}


producer = Producer({
    'bootstrap.servers': config['servers'],
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': config['username'],
    'sasl.password': config['password']
})

consumer = Consumer({
    'bootstrap.servers': config['servers'],
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': config['username'],
    'sasl.password': config['password'],
    'group.id': 'todo-in',
    'auto.offset.reset': 'latest'
})


def main():
    AppRunner(
        app=GuestList(),
        producer=producer,
        consumer=consumer
    ).start()


if __name__ == '__main__':
    main()
