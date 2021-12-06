# RabbitMQ

## Send message with Curl to Vhost awx

```bach
curl -u smax:wVuadmdlt4ShBxMvMqHLmBN0sB8wgXDD -H "content-type:application/json" -X POST -d'{
    "properties": {},
    "routing_key":"hello_1",
    "payload":"HI from curl",
    "payload_encoding":"string"
    }' http://localhost:15672/api/exchanges/awx/amq.default/publish

```

## craete queues in awx vhost

```bach

curl -i -u default_user_xeAtZ3fNuxwSWuKr0DQ:wVuadmdlt4ShBxMvMqHLmBN0sB8wgXDD -H "content-type:application/json" \
-X PUT -d'{"durable":true}' \
http://localhost:15672/api/queues/awx/hello_1
```

## Durable

Set message delivery mode to persistent
