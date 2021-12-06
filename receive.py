#!/usr/bin/env python
import pika, sys, os

from pika import credentials


def main():

    cred = pika.PlainCredentials(
        username="default_user_xeAtZ3fNuxwSWuKr0DQ",
        password="wVuadmdlt4ShBxMvMqHLmBN0sB8wgXDD",
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="localhost", credentials=cred, virtual_host="awx"
        )
    )
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        # Ack messages in callback funtion
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=False)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
