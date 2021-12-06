#!/usr/bin/env python
import pika


cred = pika.PlainCredentials(
    username="default_user_dvrJ8aj7QB0LaXwrHKd",
    password="-GVO62hfPPNpa3Q8lTGx1--x6yk-5gzI",
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", credentials=cred, virtual_host="awx")
)
channel = connection.channel()

channel.queue_declare(queue="hello", durable=True)


msg = "Hello smax!"
channel.basic_publish(exchange="", routing_key="hello", body=msg)
print(f" [x] Sent '{msg}'")
connection.close()
