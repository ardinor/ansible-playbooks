### Sensu-Client ###

Installs a [Sensu](http://sensuapp.org) client.

##### Setup

Comes with some pre-generated SSL certs for testing, but before deploying you should create your own using the notes [here](http://sensuapp.org/docs/latest/ssl). Place the certificate and the key in files/ overwriting the existing ones.

RabbitMQ settings (how the client communicates with the master) are set in vars/main.yml and should be changed, the values defined there are:
 - rabbitmq_host_ip: 127.0.0.1
 - rabbitmq_host_port: 8159
 - rabbitmq_password: password

Some default are also defined in defaults/main.yml

 - rabbitmq_vhost: sensu
 - rabbitmq_user: sensu

These can be overwritten if your setup is different.

##### Checks

Checks defined in the `checks` dictionary in vars/main.yml are installed locally and the config file for the check itself is installed on the sensu master server. Checks defined in the `checks` dictionary are in the format:

    checks:
      "{{ check_name }}":
        file: "{{ file_name }}"
        url: "{{ url }}"

They are downloaded from `{{ url }}` saved as `{{ file_name }}` in /etc/sensu/plugins/

Checks with 'metric' in the name are set with the graphite handler to ship the metrics data off to a graphite instance as defined by the sensu master.

Several metrics are installed by default

 - check_load
 - check_cpu
 - check_disk
 - cpu_metrics
 - vmstat_metrics
 - memory_metrics
 - load_metrics
 - uptime_metrics

To remove any of these, just delete them out of vars/main.yml

TO DO:
-------

- Some flag for setting dev/prod subscriptions in client.json
