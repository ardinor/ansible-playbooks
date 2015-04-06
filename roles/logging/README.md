### Logging Playbook ###

Ansible playbook for setting up logging. When the variable `docker_logging` is true, it will provide logging for Docker containers using logspout to collect logs from containers and a logstash Docker container as the collecter of logs. The logstash container exposes port 5545 and can accept logs from the host itself.

The logstash instance expects a redis host to ship the logs off to, if one is not provided by the environment variables `REDIS_HOST` and `REDIS_PORT` all logs received will be sent to stdout.

TO DO:
---------

- Syslog stuff
