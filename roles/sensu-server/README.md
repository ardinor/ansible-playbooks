### Sensu-Server (Sensu-Master) ###

Installs a [Sensu](http://sensuapp.org) Master server. Installs a Sensu client on itself as well. Has default support for shipping metrics to Graphite.

Comes with some pre-generated SSL certs for testing, but before deploying you should create your own using the notes [here](http://sensuapp.org/docs/latest/ssl). Place the certificate, private key and CA certificate in files/ overwriting the existing ones.

The sensu-client role installs the sensu-client on servers that are to be monitored and any checks that it adds are automatically installed on this server.

There are several defaults defined (in defaults/main.yml) that work on the assumption that RabbitMQ, Redis, Graphite, Sensu and Uchiwa all operate on the same host and on the default ports. To change any of these feel free to overwrite them.

In vars/main.yml two variables are defined:

 - rabbitmq_password: password
 - datacenter_name: sensu

At the very least, the `rabbitmq_password` should be changed before deployment.

TO DO:
-------

- Some flag for setting dev/prod subscriptions in client.json
- Work on checks and handlers
- Work on making the Graphite handler optional
